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

    
    def loadLevel(self, *args, **kwargs ):
        # self.feet.clear()
        for i in range(6):
            args = footDic[random.randint(0, len(footDic) - 1)]
            foot = Foot(args["legsPath"], args["footPath"], args["unhappyPath"], args["happyPath"], args["hasLaces"], i)
            self.feet.append(foot)
        
        self.isActive = True
        super().loadLevel()
    
    def unloadLevel(self):
        self.isActive = False
        self.feet.clear()
        super().unloadLevel()

    def onMouseMoved(self, pos):
        self.player.follow_mouse(pos)

    def update(self, surface=None):
        event_bus.publish(
            "add_surface_to_render",
            self.background,
            [1024/2, 640/2],
            0  
        )
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
                print("foot: ", foot)
                loadLevel = LoadLevelCommand("shoes", foot)
                event_bus.publish("queue_command", loadLevel)
                return
            
        self.player.update()
    