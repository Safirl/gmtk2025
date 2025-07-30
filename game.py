import os
import pygame
from pygame import Vector2
from screeninfo import get_monitors

os.environ['SDL_VIDEO_CENTERED'] = '1'

class UserInterface():
    def __init__(self):
        for monitor in get_monitors():
            if monitor.is_primary:
                mainMonitor = monitor
        if (not mainMonitor):
            pygame.quit()    
                
        self.worldSize = Vector2(mainMonitor.width, mainMonitor.height)

        self.window = pygame.display.set_mode(self.worldSize)
        pygame.display.set_caption("My game")
        
    def render(self):
        self.window.fill((0,0,0))
        #render sprites on screen
        pygame.draw.rect(self.window,(0,0,255),(120,120,400,240))
        pygame.display.update()
        pass
        

class Game():
    def __init__(self):
        pygame.init()
        self.ui = UserInterface()
        self.clock = pygame.time.Clock()
        self.running = True
    
    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        pass
    
    def update(self):
        #handle logic directly related to the game (score, load level, )
        pass
    
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.ui.render()        
            self.clock.tick(60)
        
game = Game()
game.run()

pygame.quit()