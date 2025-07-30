import os
import pygame
from pygame import Vector2

os.environ['SDL_VIDEO_CENTERED'] = '1'

class UserInterface():
    def __init__(self):
        self.cellSize = Vector2(64,64)
        self.worldSize = Vector2(16, 10)

        windowSize = self.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x),int(windowSize.y)))
        pygame.display.set_caption("My game")
        
    def render(self):
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
        #handle inputs
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