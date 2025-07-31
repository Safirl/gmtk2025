import pygame
import random
from foot import Foot

from level import Level

# LOAD IMAGES ONCES
legImage = [
            pygame.image.load("assets/legs/legs1.png"),
            pygame.image.load("assets/legs/legs2.png"),
            pygame.image.load("assets/legs/legs3.png"),
            pygame.image.load("assets/legs/legs4.png")
        ]

class StreetLevel(Level):
    def __init__(self):
        super().__init__("street")
        self.feet = []
    
    def loadLevel(self):
        super().loadLevel()
        for i in range(11):
            foot = Foot(legImage)
            foot.getRandomLegs()
            i = i+1
            self.feet.append(foot)


    def unloadLevel(self):
        super().unloadLevel()
        self.feet.clear()
    
    def update(self, surface):
        for foot in self.feet:
            foot.draw(surface)

        pygame.display.flip()
        

