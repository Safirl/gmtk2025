from level import Level
from eventBus import event_bus
from command import Command
from foot import Foot
import pygame
from pygame import Vector2, Surface, Rect
import os
import numpy

seuil = 4

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
        self.lacesTexture = pygame.image.load(self.foot.lacesPath)
        self.drawnLacesSurface = Surface((1024, 640), pygame.SRCALPHA)
        self.isMousePressed = False
        self.lastMousePos: tuple[int,int] = None
        self.mousePos: tuple[int,int] = None
        
        event_bus.subscribe('mouse_moved', self.onMouseMoved)
        event_bus.subscribe('mouse_down', self.onMouseDown)
        event_bus.subscribe('mouse_up', self.onMouseUp)
        
        return super().loadLevel()

    def unloadLevel(self):
        event_bus.unsubscribe('mouse_moved', self.onMouseMoved)
        event_bus.unsubscribe('game_update', self.onUpdate)
        return super().unloadLevel()

    def update(self):
        event_bus.publish("add_surface_to_render", self.footTexture, [1024/2, 640/2], 1)
        event_bus.publish("add_surface_to_render", self.lacesTexture, [1024/2, 640/2], 2)
        if not self.foot.hasLaces:
            return
        if self.isMousePressed:
            rect = Rect(self.mousePos[0], self.mousePos[1], 10, 10)
            pygame.draw.line(self.drawnLacesSurface, (0, 0, 255), self.lastMousePos, self.mousePos, 15)
        
        super().update()

    def onMouseMoved(self, newPos):
        if self.mousePos is not None:
            self.lastMousePos = self.mousePos
        self.mousePos = newPos
        event_bus.publish("add_surface_to_render", self.drawnLacesSurface, [1024/2,640/2], 3)
        command = ShoesMouseMovedCommand(newPos, self.armTexture)
        event_bus.publish("queue_command", command)
    
    def onMouseDown(self, newPos):
        self.isMousePressed = True
        
    def onMouseUp(self):
        self.isMousePressed = False
        alphaTexture = pygame.image.load(self.foot.alphaLacesPath)
        command = CompleteLacesCommand(self.drawnLacesSurface, alphaTexture)
        event_bus.publish("queue_command", command)
    

class CompleteLacesCommand(Command):
    def __init__(self, lacesTexture: Surface, completeLacesAlphatexture: Surface):
        self.lacesTexture = lacesTexture
        self.completeLacesTexture = completeLacesAlphatexture
    
    def run(self):
        diff = self.getAlphaDifferencePercentage(self.lacesTexture, self.completeLacesTexture)
        if diff >= seuil:
            print("you lost! :", diff)
        else:
            print("you won! :", diff)
    
    def getAlphaDifferencePercentage(self, texture1: Surface, texture2: Surface):
        if texture1.get_size() != texture2.get_size():
            return
        
        alpha1 = pygame.surfarray.pixels_alpha(texture1)
        alpha2 = pygame.surfarray.pixels_alpha(texture2)
        
        diff = numpy.abs(alpha1.astype(int) - alpha2.astype(int))
        
        total_pixels = alpha1.shape[0] * alpha1.shape[1]
        max_diff = 255 * total_pixels
        percent_diff = numpy.sum(diff) / max_diff * 100
        
        return percent_diff
        
    
class ShoesMouseMovedCommand(Command):
    def __init__(self, newPos, armTexture: Surface):
        self.pos = Vector2(newPos)
        self.pos.y += armTexture.get_height()/2
        self.armTexture = armTexture
    
    def run(self):
        event_bus.publish("add_surface_to_render", self.armTexture, [self.pos[0], self.pos[1]], 4)
        pass
    