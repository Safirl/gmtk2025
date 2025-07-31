import random
class Foot():
    def __init__(self, legsPath="", footPath="", hasLaces=True):
        self.legsPath : str = legsPath
        self.footPath : str = footPath
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        self.hasLaces = hasLaces

        self.foots = [
    {
        "legs": "assets/legs1.png",
        "foot": "",
        "hasLaces": True
    },
    {
        "legs": "assets/legs2.png",
        "foot": "",
        "hasLaces": True
    },
    {
        "legs": "assets/legs3.png",
        "foot": "",
        "hasLaces": True
    },
    {
        "legs": "assets/legs4.png",
        "foot": "",
        "hasLaces": True
    },
]


        
    def animate(seft):
        pass

    def clear(self):
        pass
    


    def getRandomLegs(self):
        # self.legs = random.choice(self.foots["legs"])
        pass
    
    def draw(self, surface):
        # if self.legs:
        #     surface.blit(self.legs, (self.x, self.y))
        pass
