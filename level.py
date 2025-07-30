class Level():
    def __init__(self, name: str):
        self.name = name
        pass
    
    def loadLevel(self):
        print(f'Loading level: {self.name}')
        pass
    
    def unloadLevel(self):
        print(f'Unloading level: {self.name}')
        pass

    def update(self):
        raise NotImplementedError
    





