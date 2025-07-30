from command import Command
class LevelLoader():
    def __init__(self):
        self.levels = {
            "mainScreen": MainScreenLevel(),
            "gameOverScreen": GameOverLevel(),
            "street": StreetLevel(),
            "shoes": ShoesLevel()
        }
        self.currentLevel : Level = None
        
        pass
    
    def changeLevel(self, levelName: str):
        if self.currentLevel:
            self.currentLevel.unloadLevel()
            self.currentLevel = None
            
        self.currentLevel = self.levels.get(levelName)
        if self.currentLevel:
            self.currentLevel.loadLevel()
        else:
            print(f"Level '{levelName}' not found.")
        
        pass
    
    
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
    
class MainScreenLevel(Level):
    def __init__(self):
        super().__init__("mainScreen")        
        pass
    
    def loadLevel(self):
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
    
class GameOverLevel(Level):
    def __init__(self):
        super().__init__("gameOverScreen")
        pass
    
    def loadLevel(self):
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
    
class StreetLevel(Level):
    def __init__(self):
        super().__init__("street")
        pass
    
    def loadLevel(self):
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
    
class ShoesLevel(Level):
    def __init__(self):
        super().__init__("shoes")
        pass
    
    def loadLevel(self):
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()



class LoadLevelCommand(Command):
    def __init__(self,levelName:str):
        self.levelName = levelName

    def run(self):
        levelLoader.changeLevel(self.levelName)
        pass

levelLoader = LevelLoader()