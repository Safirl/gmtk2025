from game import Game
class Command():
    def  __init__(self, game : Game):
        if not game :
            print('Game is not valid')
            return
        self.game = game
    
    def run():
        raise NotImplementedError()




class LoadLevelCommand(Command):
    def __init__(self, levelName:str):
        super().__init__(self)
        self.levelName = levelName
    
    def run(self):
        super().run()
        self.game.levelLoader.changeLevel(self.levelName)

