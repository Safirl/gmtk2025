import pygame
import random
from foot import Foot
from level import Level
from eventBus import event_bus
from player import Player

# LOAD IMAGES ONCES
legsPath = [
            pygame.image.load("assets/legs/legs1.png"),
            pygame.image.load("assets/legs/legs2.png"),
            pygame.image.load("assets/legs/legs3.png"),
            pygame.image.load("assets/legs/legs4.png")
        ]

class StreetLevel(Level):
    def __init__(self):
        super().__init__("street")
        self.feet = []
        self.player = Player()
        self.background = pygame.image.load("assets/backgroundStreet.png")
        self.isActive = False
        print("StreetLevel initialized") 

    
    def loadLevel(self, *args, **kwargs ):
        print("Street screen loaded.")
        super().loadLevel()
        self.feet.clear()
        for i in range(6):
            foot = Foot(index=i)
            print(f"Created foot {i}")  
            self.feet.append(foot)
        
        self.isActive = True
        event_bus.subscribe('game_update', self.update)
    
    def unloadLevel(self):
        print("Unloading street level")
        self.isActive = False
        event_bus.unsubscribe('game_update', self.update)
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
                print(f"Leg detected! Sprite: {foot.legsPath}")
                self.unloadLevel()  # Décharge le niveau actuel
                event_bus.publish("load_level", "shoes", foot)
                return
            
        self.player.update()
    