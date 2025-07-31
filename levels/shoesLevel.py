from level import Level
from eventBus import event_bus
from command import Command
from foot import Foot
import pygame
from pygame import Vector2, Surface
import os

class ShoesLevel(Level):
    def __init__(self):
        super().__init__("shoes")
        self.armTexture = pygame.image.load("assets/armPicking.png")

    def loadLevel(self, foot: Foot):
        if not foot:
            print("Foot is not valid for level: ", self.name)
            return
        self.foot = foot
        event_bus.subscribe('mouse_moved', self.onMouseMoved)
        event_bus.subscribe('game_update', self.onUpdate)
        
        return super().loadLevel()

    def unloadLevel(self):
        event_bus.unsubscribe('mouse_moved', self.onMouseMoved)
        event_bus.unsubscribe('game_update', self.onUpdate)
        return super().unloadLevel()

    def onUpdate(self):
        command = ShowFootCommand(self.foot, Vector2(1024/2, 640/2))
        event_bus.publish("queue_command", command)
        if not self.foot.hasLaces:
            return
        
        super().update()

    def onMouseMoved(self, newPos):
        #print(f"Mouse moved in shoes level: {newPos}")
        command = ShoesMouseMovedCommand(newPos, self.armTexture)
        event_bus.publish("queue_command", command)
        
        
class ShoesMouseMovedCommand(Command):
    def __init__(self, newPos, armTexture: Surface):
        self.pos = Vector2(newPos)
        self.pos.y += armTexture.get_height()/2
        self.armTexture = armTexture
    
    def run(self):
        event_bus.publish("add_surface_to_render", self.armTexture, [self.pos[0], self.pos[1]], 2)
        pass
    
class ShowFootCommand(Command):
    def __init__(self, foot: Foot, position):
        self.foot = foot
        self.position = position
    
    def run(self):
        if not os.path.isfile(self.foot.footPath):
            print(f"Image not found: {self.foot.footPath}")
            return
        texture = pygame.image.load(self.foot.footPath)
        event_bus.publish("add_surface_to_render", texture, [self.position.x, self.position.y], 1)
        