from level import Level
from command import Command
from levels.mainScreenLevel import MainScreenLevel
from levels.gameoverLevel import GameOverLevel
from levels.streetLevel import StreetLevel
from levels.shoesLevel import ShoesLevel

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
    

class LoadLevelCommand(Command):
    def __init__(self,levelName:str):
        self.levelName = levelName

    def run(self):
        levelLoader.changeLevel(self.levelName)
        pass

levelLoader = LevelLoader()
    