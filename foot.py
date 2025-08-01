import random
import pygame
class Foot():
    def __init__(self, legsPath="", footPath="", alphaLacesPath="", lacesPath="", hasLaces=True, index=0):
            
        self.foots = [
            {
                "legs": "assets/legs/legs1.png",
                "foot": "assets/foot.jpg",
                "hasLaces": True
            },
            {
                "legs": "assets/legs/legs2.png",
                "foot": "assets/foot.jpg",
                "hasLaces": True
            },
            {
                "legs": "assets/legs/legs3.png",
                "foot": "assets/foot.jpg",
                "hasLaces": True
            },
            {
                "legs": "assets/legs/legs4.png",
                "foot": "assets/foot.jpg",
                "hasLaces": True
            },
            ]
        selected_foot = random.choice(self.foots)
        self.legsPath = pygame.image.load(selected_foot["legs"])
        self.footPath = selected_foot["foot"]
        self.lacesPath = selected_foot["laces"]
        self.hasLaces = selected_foot["hasLaces"]
        self.alphaLacesPath = alphaLacesPath

        self.x = random.randint(0, 700)
        self.y = -500 - (index * 500)
        self.speed = 5
        self.hasLaces = hasLaces
        self.index = index
        self.original_image = legsPath 
        self.scale = 1.0  

        self.width = 300
        self.height = 400
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)




        
    def animate(seft):
        pass

    def clear(self):
        pass
    
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
        return pygame.transform.scale(self.original_image, (new_width, new_height))
    
    def reset_position(self):
        self.y = -2500
        self.x = random.randint(0, 700)
        self.rect.x = self.x
        self.rect.y = self.y
        print('is reset', self.index)

    # def getRandomLegs(self):
    #     # self.legs = random.choice(self.foots["legs"])
    #     pass
    
    def draw(self, surface):
        if self.legsPath:
            surface.blit(self.legsPath, (self.x, self.y))
