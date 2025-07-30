from level import Level
from command import Command
from eventBus import event_bus

class LoadLevelCommand(Command):
    def __init__(self, levelName: str):
        self.levelName = levelName

    def run(self):
        event_bus.publish('load_level', self.levelName)

class LevelLoader():
    def __init__(self):
        # Import des niveaux ici pour éviter les imports circulaires
        from levels.mainScreenLevel import MainScreenLevel
        from levels.gameoverLevel import GameOverLevel
        from levels.streetLevel import StreetLevel
        from levels.shoesLevel import ShoesLevel
        
        self.levels = {
            "mainScreen": MainScreenLevel(),
            "gameOverScreen": GameOverLevel(),
            "street": StreetLevel(),
            "shoes": ShoesLevel()
        }
        self.currentLevel = None
        
        # S'abonner à l'événement de chargement de niveau
        event_bus.subscribe('load_level', self.changeLevel)

    def changeLevel(self, levelName: str):
        if self.currentLevel:
            self.currentLevel.unloadLevel()
            self.currentLevel = None
        
        self.currentLevel = self.levels.get(levelName)
        if self.currentLevel:
            self.currentLevel.loadLevel()
        else:
            print(f"Level '{levelName}' not found.")