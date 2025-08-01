from level import Level
from eventBus import event_bus
from command import Command, LoadLevelCommand
from foot import Foot, laces
import pygame
from pygame import Vector2, Surface, Rect
import os
import numpy
from random import randint

seuil = 5.

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
        self.lacesTexture, self.alphaLacesTexture = self.LoadRandomLaces()
        self.roadTexture = pygame.image.load("assets/shoesLevel/road.jpg")
        
        event_bus.subscribe('mouse_moved', self.onMouseMoved)
        event_bus.subscribe('mouse_down', self.onMouseDown)
        event_bus.subscribe('mouse_up', self.onMouseUp)
        
        #Draw static items
        event_bus.publish("add_surface_to_render", self.footTexture, [1024/2, 640/2], 1, True)
        event_bus.publish("add_surface_to_render", self.roadTexture, [1024/2, 640/2], 0, True)
        
        if self.foot.hasLaces:
            event_bus.publish("add_surface_to_render", self.lacesTexture, [1024/2, 640/2], 2, True)
        
        self.isLevelRunning = True
        return super().loadLevel()

    def unloadLevel(self):
        event_bus.unsubscribe('mouse_moved', self.onMouseMoved)
        event_bus.unsubscribe('mouse_down', self.onMouseDown)
        event_bus.unsubscribe('mouse_up', self.onMouseUp)
        self.isLevelRunning = False
        return super().unloadLevel()

    def update(self):
        if not self.isLevelRunning:
            return
        if not self.foot.hasLaces:
            command = CompleteLacesCommand(self.foot, self.drawnLacesSurface, self.alphaLacesTexture, self)
            event_bus.publish("queue_command", command)
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
        
    def onMouseUp(self, pos):
        if not self.isLevelRunning:
            return
        self.isMousePressed = False
        command = CompleteLacesCommand(self.foot, self.drawnLacesSurface, self.alphaLacesTexture, self)
        event_bus.publish("queue_command", command)
        
    def LoadRandomLaces(self):
        random = laces[randint(0, len(laces) - 1)]
        alphaTexture = pygame.image.load(random["alphaLacesPath"])
        lacesTexture = pygame.image.load(random["lacesPath"])
        return lacesTexture, alphaTexture
    

class CompleteLacesCommand(Command):
    def __init__(self, foot: Foot, drawnTexture: Surface, alphaTexture: Surface, level: ShoesLevel):
        self.foot = foot
        self.drawnTexture = drawnTexture
        self.alphaTexture = alphaTexture
        self.level = level
    
    def run(self):
        self.level.isLevelRunning = False
        diff = self.getAlphaDifferencePercentage(self.alphaTexture, self.drawnTexture)
        faceTexture = None
        if diff >= seuil:
            event_bus.publish("on_timer_changed", -3.)
            faceTexture = pygame.image.load(self.foot.unhappyPath)
        else:
            event_bus.publish("on_timer_changed", 3.)
            faceTexture = pygame.image.load(self.foot.happyPath)
            
        event_bus.publish("add_surface_to_render", faceTexture, [1024-faceTexture.get_width()/2,0+faceTexture.get_height()/2], 4, True)
        
        loadLevel = LoadLevelCommand("street")
        event_bus.publish("queue_delayed_command", 1.5, loadLevel)
    
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
    