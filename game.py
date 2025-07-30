import os
import pygame
from pygame import Vector2
from screeninfo import get_monitors
from eventBus import event_bus

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
        # render sprites on screen
        pygame.draw.rect(self.window,(0,0,255),(120,120,400,240))
        pygame.display.update()

class Game():
    def __init__(self):
        pygame.init()
        self.ui = UserInterface()
        self.commands = []
        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
                event_bus.publish('mouse_moved', mousePos)

    def update(self):
        event_bus.publish('game_update')
        for command in self.commands:
            command.run()
        self.commands.clear()

    def queueCommand(self, command):
        self.commands.append(command)

    def loadLevel(self, levelName):
        event_bus.publish('load_level', levelName)

    def run(self):
        # Charger le niveau initial après que tout soit prêt
        self.loadLevel("shoes")
        
        while self.running:
            self.processInput()
            self.update()
            self.ui.render()
            self.clock.tick(60)