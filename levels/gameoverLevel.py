from level import Level
import pygame
from eventBus import event_bus

class GameOverLevel(Level):
    def __init__(self):
        super().__init__("gameOverScreen")
        self.background = pygame.image.load("assets/gameOverBackground.jpg")
        
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
        event_bus.publish("clean_queued_commands")
        event_bus.publish("add_surface_to_render", self.background, [1024/2, 640/2], 0, True)
        event_bus.publish("change_music", "assets/sounds/sneaky-end.mp3")
        
        super().loadLevel()

    def unloadLevel(self):
        super().unloadLevel()
