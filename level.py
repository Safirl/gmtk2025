class Level:
    def __init__(self, name):
        self.name = name

    def loadLevel(self, *args, **kwargs):
        print(f"Loading level {self.name}")

    def unloadLevel(self):
        print(f"Unloading level for {self.name}")

    def update(self):
        pass
    

