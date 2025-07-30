class Level:
    def __init__(self, name):
        self.name = name

    def loadLevel(self):
        print(f"Base load for {self.name}")

    def unloadLevel(self):
        print(f"Base unload for {self.name}")

    def update(self):
        pass
    

