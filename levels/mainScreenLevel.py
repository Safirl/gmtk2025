from level import Level
import pygame
from eventBus import event_bus

class MainScreenLevel(Level):
    def __init__(self):
        super().__init__("mainScreen")
        
        self.menuItems = [
        {
            'title': 'Let\'s tie some shoes !',
            'action': lambda: self.loadLevel("level1.tmx")
        },
        {
            'title': 'Credits',
            'action': lambda: self.loadLevel("level2.tmx")
        },
        {
            'title': 'Quit',
            'action': lambda: self.exitMenu()
        }
    ]
    
    def loadLevel(self):
        super().loadLevel()
        pygame.font.init()
        h1 = pygame.font.Font("assets/fonts/Bubble.ttf", 42)
        self.buttonFont = pygame.font.Font("assets/fonts/Bubble.ttf", 24)
        self.title = h1.render("C'est bouclé !", True, (255,255,255,255))

    def unloadLevel(self):
        super().unloadLevel()
    
    def update(self):
        titlePos = (self.title.get_size()[0]/2 + 64, self.title.get_size()[1]/2 + 64)
        event_bus.publish("add_surface_to_render", self.title, [titlePos[0], titlePos[1]], 10)
        for item in self.menuItems:
            button = self.buttonFont.render(item["title"], True, (255,255,255,255))
            event_bus.publish("add_surface_to_render", button, [titlePos[0] + 64, titlePos[1] + 64], 10)