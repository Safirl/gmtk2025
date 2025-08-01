import random
import pygame
from eventBus import event_bus

#laces drawing
laces = [
    {
        "alphaLacesPath": "assets/alpha/laces1Alpha.png",
        "lacesPath": "assets/laces/laces1.png"
    },
    {
        "alphaLacesPath": "assets/alpha/laces2Alpha.png",
        "lacesPath": "assets/laces/laces2.png"
    },
    {
        "alphaLacesPath": "assets/alpha/laces3Alpha.png",
        "lacesPath": "assets/laces/laces3.png"
    },
    {
        "alphaLacesPath": "assets/alpha/laces4Alpha.png",
        "lacesPath": "assets/laces/laces4.png"
    },
]

footDic = [
    {
        "legsPath": "assets/legs/characterRedShoes1.PNG",
        "footPath": "assets/foot/redFoot.png",
        "unhappyPath": "assets/reactions/characterRedShoesAngry.png",
        "happyPath": "assets/reactions/characterRedShoesHappy.png",
        "neutralPath": "assets/reactions/characterRedShoesSurprised.png",
        "hasLaces": True,
    },
    {
        "legsPath": "assets/legs/characterBrownShoes.png",
        "footPath": "assets/foot/brownFoot.png",
        "unhappyPath": "assets/reactions/characterBrownShoesAngry.png",
        "happyPath": "assets/reactions/characterBrownShoesHappy.png",
        "neutralPath": "assets/reactions/characterBrownShoesSurprised.png",
        "hasLaces": True
    },
]

class Foot():
    def __init__(self, legsPath="", footPath="", unhappyPath="", happyPath="", hasLaces=True, index=0, neutralPath=""):
            
        self.unhappyPath = unhappyPath
        self.happyPath = happyPath
        self.neutralPath = neutralPath
        self.legsImage = pygame.image.load(legsPath)
        self.footImage = pygame.image.load(footPath)
        self.hasLaces = hasLaces

        self.x = random.randint(0, 700)
        self.y = -500 - (index * 500)
        self.speed = 5
        self.index = index
        self.scale = 1.0

        self.width = 300
        self.height = 409
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height*0.80)

    def move(self):
        self.y += self.speed  
        self.rect.y = self.y
        self.rect.x = self.x
        if self.rect.bottom > 1024: 
            self.reset_position()
    
    def get_scaled_image(self):
        self.scale = 0.5 + (self.y / 640)
        self.scale = max(0.5, min(1.5, self.scale))
        new_width = int(self.width * self.scale)
        new_height = int(self.height * self.scale)
        return pygame.transform.scale(self.legsImage, (new_width, new_height))
    
    def reset_position(self):
        self.y = -2500
        self.x = random.randint(0, 700)
        self.rect.x = self.x
        self.rect.y = self.y
        print('is reset', self.index)
