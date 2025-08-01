import pygame
import random
from foot import Foot, footDic
from level import Level
from eventBus import event_bus
from player import Player
from command import LoadLevelCommand

class StreetLevel(Level):
    def __init__(self):
        super().__init__("street")
        self.feet = []
        self.player = Player()
        self.background = pygame.image.load("assets/backgroundStreet.png")
        self.isActive = False

    
    def loadLevel(self, *args, **kwargs):
        # self.feet.clear()
        for i in range(6):
            footArgs = footDic[random.randint(0, len(footDic) - 1)]
            foot = Foot(footArgs["legsPath"], footArgs["footPath"], footArgs["unhappyPath"], footArgs["happyPath"], footArgs["hasLaces"], i, footArgs["neutralPath"])
            self.feet.append(foot)
        
        self.isActive = True
        event_bus.publish(
            "add_surface_to_render",
            self.background,
            [1024/2, 640/2],
            0,
            True
        )
        super().loadLevel()
    
    def unloadLevel(self):
        self.isActive = False
        self.feet.clear()
        super().unloadLevel()

    def onMouseMoved(self, pos):
        self.player.follow_mouse(pos)

    def update(self, surface=None):
        if not self.isActive:
            return
        for foot in self.feet:
            foot.move()
            scaled_image = foot.get_scaled_image()
            event_bus.publish(
                "add_surface_to_render",
                scaled_image,  
                [foot.x, foot.y],
                1
            )
            if foot.rect.colliderect(self.player.rect):
                texture = pygame.image.load(foot.neutralPath)
                event_bus.publish("add_surface_to_render", texture, [1024-texture.get_width()/2,0+texture.get_height()/2], 4, True)
                loadLevel = LoadLevelCommand("shoes", foot)
                event_bus.publish("queue_delayed_command", 1.5, loadLevel)
                self.isActive = False
                return
            
        self.player.update()
    