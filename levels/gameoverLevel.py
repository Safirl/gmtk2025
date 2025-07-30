from level import Level
class GameOverLevel(Level):
    def __init__(self):
        super().__init__("gameOverScreen")
        pass
    
    def loadLevel(self):
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
