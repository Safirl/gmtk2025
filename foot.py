import random
class Foot():
    def __init__(self):
        self.legs : str = ""
        self.foot : str = ""
        self.x = random.randint(0, 700)
        self.y = random.randint(0, 500)
        hasLaces: bool

        self.legsOptions = [
            "assets/legs1.png",
            "assets/legs2.png",
            "assets/legs3.png",
            "assets/legs4.png"
        ]
    def __init__(self, legsPath="", footPath="", hasLaces=True):
        self.legsPath = legsPath
        self.footPath = footPath
        self.hasLaces = hasLaces
    
    def animate(seft):
        pass

    def clear(self):
        pass
    
foots = [
    {
        "legs": "",
        "foot": "",
        "hasLaces": True
    },
    {
        "legs": "",
        "foot": "",
        "hasLaces": True
    },
    {
        "legs": "",
        "foot": "",
        "hasLaces": True
    },
    {
        "legs": "",
        "foot": "",
        "hasLaces": True
    },
]

    def getRandomLegs(self):
        self.legs = random.choice(self.legsOptions)
    
    def draw(self, surface):
        if self.legs:
            surface.blit(self.legs, (self.x, self.y))
