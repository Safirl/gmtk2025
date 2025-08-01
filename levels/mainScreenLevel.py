from level import Level
import pygame
from eventBus import event_bus
from command import QuitGameCommand, Command

class MainScreenLevel(Level):
    def __init__(self):
        super().__init__("mainScreen")
        
        self.menuItems = [
            {
                'title': 'Play! Let\'s tie some shoes...',
                'action': lambda: self.startGame(),
            },
            {
                'title': 'Credits',
                'action': lambda: print('Credits')
            },
            {
                'title': 'Quit',
                'action': lambda: self.quitGame()
            }
        ]
        self.buttonRects = []

    def loadLevel(self):
        super().loadLevel()
        self.background = pygame.image.load("assets/backgroundStreet.png")
        event_bus.publish("add_surface_to_render", self.background, [1024/2, 640/2], 0, True)
        
        pygame.font.init()
        h1 = pygame.font.Font("assets/fonts/Bubble.ttf", 42)
        self.buttonFont = pygame.font.Font("assets/fonts/Gowun.ttf", 32)
        self.title = h1.render("C'est bouclé !", True, (255,255,255,255))
        self.buttonRects.clear()

        event_bus.subscribe("mouse_up", self.onMouseUp)
        
        self.music = pygame.mixer.music.load("assets/sounds/sneaky-feet.mp3")
        pygame.mixer.music.play(-1)
        
        self.isRunning = True

    def unloadLevel(self):
        super().unloadLevel()
        event_bus.unsubscribe("mouse_up", self.onMouseUp)
        self.isRunning = False

    def update(self):
        titlePos = (self.title.get_width() / 2 + 64, self.title.get_height() / 2 + 64)
        event_bus.publish("add_surface_to_render", self.title, [titlePos[0], titlePos[1]], 10)

        self.buttonRects.clear()
        i = 1
        for item in self.menuItems:
            button = self.buttonFont.render(item["title"], True, (255,255,255,255))
            buttonPos = (64, 128 + 64 * i)  # Position fixe sur X
            event_bus.publish("add_surface_to_render", button, [buttonPos[0] + button.get_size()[0]/2, buttonPos[1] + button.get_size()[1]/2], 10)

            rect = button.get_rect(topleft=buttonPos)
            self.buttonRects.append((rect, item["action"]))
            i += 1

    def onMouseUp(self, pos):
        if not self.isRunning:
            return
        for rect, action in self.buttonRects:
            if rect.collidepoint(pos):
                action()
                
    def startGame(self):
        self.isRunning = False
        command = StartGameCommand()
        pygame.mixer.music.fadeout(1500)
        event_bus.publish("queue_delayed_command", 1.5, command)
        
    def quitGame(self):
        command = QuitGameCommand()
        event_bus.publish("queue_command", command)

class StartGameCommand(Command):
    def __init__(self):
        super().__init__()
        
    def run(self):
        event_bus.publish("start_game")