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
        "legsPath": "assets/legs/characterRedShoes.PNG",
        "footPath": "assets/foot/redFoot.png",
        "unhappyPath": "assets/reactions/characterRedShoesAngry.png",
        "happyPath": "assets/reactions/characterRedShoesHappy.png",
        "neutralPath": "assets/reactions/characterRedShoesSurprised.png",
        "hasLaces": True,
        "streetSound": "assets/sounds/bruitages/redC/ohNo.mp3",
        "successSound": "assets/sounds/bruitages/redC/amazing.mp3",
        "failSound": "assets/sounds/bruitages/redC/ruinedDay.mp3"
    },
    {
        "legsPath": "assets/legs/characterBrownShoes.png",
        "footPath": "assets/foot/brownFoot.png",
        "unhappyPath": "assets/reactions/characterBrownShoesAngry.png",
        "happyPath": "assets/reactions/characterBrownShoesHappy.png",
        "neutralPath": "assets/reactions/characterBrownShoesSurprised.png",
        "hasLaces": True,
        "streetSound": "assets/sounds/bruitages/brownC/whatDoing.mp3",
        "successSound": "assets/sounds/bruitages/brownC/oweYou.mp3",
        "failSound": "assets/sounds/bruitages/brownC/run.mp3"
    },
    {
        "legsPath": "assets/legs/characterBlueShoes.webp",
        "footPath": "assets/foot/blueFoot.png",
        "unhappyPath": "",
        "happyPath": "",
        "neutralPath": "assets/reactions/characterBlueShoesSurprised.webp",
        "hasLaces": False,
        "streetSound": "assets/sounds/bruitages/brownC/whatDoing.mp3",
        "successSound": "assets/sounds/bruitages/brownC/oweYou.mp3",
        "failSound": "assets/sounds/bruitages/brownC/run.mp3"
    },
]

class Foot():
    def __init__(self, legsPath="", footPath="", unhappyPath="", happyPath="", hasLaces=True, neutralPath="", streetSound="", successSound="", failSound=""):
            
        self.unhappyPath = unhappyPath
        self.happyPath = happyPath
        self.neutralPath = neutralPath
        self.legsImage = pygame.image.load(legsPath)
        self.footImage = pygame.image.load(footPath)
        self.hasLaces = hasLaces

        self.x = random.randint(120, 800)
        self.y = -random.randint(250, 1500)
        self.speed = 5
        self.scale = 1.0

        self.width = 300
        self.height = 500
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height*0.60)

        self.sounds = [
            "assets/sounds/bruitages/mmmhhh.mp3",
            "assets/sounds/bruitages/hehe.mp3",
            "assets/sounds/bruitages/mwhaha.mp3",
            "assets/sounds/bruitages/comeHereShoes.mp3",
        ]
        self.successSound = successSound
        self.failSound = failSound
        self.streetSound = streetSound

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
        self.y = -random.randint(250, 2000)
        self.x = random.randint(120, 800)
        self.rect.x = self.x
        self.rect.y = self.y
        event_bus.publish("play_sound", self.sounds[random.randint(0, len(self.sounds)- 1)])

