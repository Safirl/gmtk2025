from level import Level
class GameOverLevel(Level):
    def __init__(self):
        super().__init__("gameOverScreen")
        
        self.menuItems = [
            {
                'title': 'Try again...',
                'action': lambda: self.startGame(),
            },
            {
                'title': 'Quit',
                'action': lambda: self.quitGame()
            }
        ]
        self.buttonRects = []
    
    def loadLevel(self, score:int):
        self.score = score
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
