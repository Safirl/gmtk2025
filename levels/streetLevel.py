import pygame
import random
from ..foot import Foot

from level import Level

LEG_IMAGES = [
            pygame.image.load("assets/legs/legs1.png").convert_alpha(),
            pygame.image.load("assets/legs/legs2.png").convert_alpha(),
            pygame.image.load("assets/legs/legs3.png").convert_alpha(),
            pygame.image.load("assets/legs/legs4.png").convert_alpha()
        ]

class StreetLevel(Level):
    def __init__(self):
        super().__init__("street")
        self.feet = []
    
    def loadLevel(self):
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
        self.feet.clear()
    
    def update(self):
        super().update()
        

