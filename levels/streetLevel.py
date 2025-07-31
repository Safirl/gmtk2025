import pygame
import random
from foot import Foot
from level import Level
from eventBus import event_bus

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

        self.background = pygame.image.load("assets/backgroundStreet.png")
        print("StreetLevel initialized") 
        print("StreetLevel initialized") 
    
    def loadLevel(self, *args, **kwargs ):
        print("Street screen loaded.")
        super().loadLevel()
        self.feet.clear()
        for i in range(6):
            leg_img = random.choice(legsPath)  
            foot = Foot(legsPath=leg_img, index=i) 
            print(f"Created foot with image: {leg_img}")  
            self.feet.append(foot)
        

        event_bus.subscribe('game_update', self.update)

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
    