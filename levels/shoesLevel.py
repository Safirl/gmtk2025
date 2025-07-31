from level import Level
from eventBus import event_bus
from command import Command
from foot import Foot
import pygame
from pygame import Vector2, Surface, Rect
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
        if not os.path.isfile(self.foot.footPath):
            print(f"Image not found: {self.foot.footPath}")
            return
        self.footTexture = pygame.image.load(self.foot.footPath)
        self.drawnLacesSurface = Surface((1024, 640), pygame.SRCALPHA)
        self.isMousePressed = False
        self.lastMousePos: tuple[int,int] = None
        self.mousePos: tuple[int,int] = None
        
        event_bus.subscribe('mouse_moved', self.onMouseMoved)
        event_bus.subscribe('mouse_down', self.onMouseDown)
        event_bus.subscribe('mouse_up', self.onMouseUp)
        event_bus.subscribe('game_update', self.onUpdate)
        
        return super().loadLevel()

    def unloadLevel(self):
        event_bus.unsubscribe('mouse_moved', self.onMouseMoved)
        event_bus.unsubscribe('game_update', self.onUpdate)
        return super().unloadLevel()

    def onUpdate(self):
        event_bus.publish("add_surface_to_render", self.footTexture, [1024/2, 640/2], 1)
        if not self.foot.hasLaces:
            return
        if self.isMousePressed:
            rect = Rect(self.mousePos[0], self.mousePos[1], 10, 10)
            pygame.draw.line(self.drawnLacesSurface, (0, 0, 255), self.lastMousePos, self.mousePos, 10)
        
        super().update()

    def onMouseMoved(self, newPos):
        if self.mousePos is not None:
            self.lastMousePos = self.mousePos
        self.mousePos = newPos
        event_bus.publish("add_surface_to_render", self.drawnLacesSurface, [1024/2,640/2], 2)
        command = ShoesMouseMovedCommand(newPos, self.armTexture)
        event_bus.publish("queue_command", command)
    
    def onMouseDown(self, newPos):
        self.isMousePressed = True
        
    def onMouseUp(self):
        self.isMousePressed = False
        pass
        
        
class CompleteLaces(Command):
    def __init__(self, lacesTexture: Surface):
        self.lacesTexture = lacesTexture
    
    def run(self):
        event_bus.publish("add_surface_to_render", self.armTexture, [self.pos[0], self.pos[1]], 2)
        pass
        
class DrawLacesCommand(Command):
    def __init__(self, newPos, surface: Surface):
        self.pos = Vector2(newPos)
        self.surface = surface
    
    def run(self):
        # texture = Surface((10, 10))
        # texture.fill((0, 0, 255))
        # rect = Rect(self.pos[0], self.pos[1], 10, 10)
        # pygame.draw.rect(self.surface,(0,0,255), rect)
        # self.surface.(self.rect.surface, self.rect.position)
        event_bus.publish("add_surface_to_render", self.surface, [1024/2,640/2], 2)
        pass
    
class ShoesMouseMovedCommand(Command):
    def __init__(self, newPos, armTexture: Surface):
        self.pos = Vector2(newPos)
        self.pos.y += armTexture.get_height()/2
        self.armTexture = armTexture
    
    def run(self):
        event_bus.publish("add_surface_to_render", self.armTexture, [self.pos[0], self.pos[1]], 2)
        pass
    