        
from eventBus import event_bus
import pygame

class Command():
    def run(self):
        raise NotImplementedError()
    
class LoadLevelCommand(Command):
    def __init__(self, levelName: str, *args, **kwargs):
        self.levelName = levelName
        self.args = args
        self.kwargs = kwargs
        
    def run(self):
        event_bus.publish("load_level", self.levelName, *self.args, **self.kwargs)
        
class QuitGameCommand(Command):
    def run(self):
        pygame.quit()
