class LevelLoader():
    def __init__(self):
        self.levels = [MainScreenLevel(), ]
        ["mainScreen","GameOverScreen", "street", "shoes"]
        self.currentLevel: Level
        
        pass
    
    def changeLevel(self, levelName: str):
        if self.currentLevel is None:
            self.currentLevel.unloadLevel()
            self.currentLevel = None
            
        self.currentLevel = self.levels[levelName]
        
        pass
    
    
class Level():
    def __init__(self, name: str):
        self.name = name
        pass
    
    def loadLevel():
        pass
    
    def unloadLevel():
        pass
    
class MainScreenLevel():
    def __init__(self):
        super.__init__(self, "mainScreen")        
        pass
    
    def loadLevel():
        pass
    
    def unloadLevel():
        pass
    
class GameOverLevel():
    def __init__(self):
        super.__init__(self, "gameOverScreen")
        pass
    
    def loadLevel():
        pass
    
    def unloadLevel():
        pass
    
class StreetLevel():
    def __init__(self):
        super.__init__(self, "street")
        pass
    
    def loadLevel():
        pass
    
    def unloadLevel():
        pass
    
class ShoesLevel():
    def __init__(self):
        super.__init__(self, "shoes")
        pass
    
    def loadLevel():
        pass
    
    def unloadLevel():
        pass