from level import Level
import pygame
from eventBus import event_bus
from command import QuitGameCommand
from command import LoadLevelCommand

class GameOverLevel(Level):
    def __init__(self):
        super().__init__("gameOverScreen")
        self.background = pygame.image.load("assets/gameOverBackground.jpg")
        
        self.menuItems = [
            {
                'title': 'Try again...',
                'action': lambda: self.loadMainMenu(),
            },
            {
                'title': 'Quit',
                'action': lambda: self.quitGame()
            }
        ]
        self.buttonRects = []
        self.sound1 = "assets/sounds/bruitages/neverTieAgain.mp3"
    
    def loadMainMenu(self):
        event_bus.publish("reset_game")
        loadLevel = LoadLevelCommand("mainScreen")
        event_bus.publish("queue_command", loadLevel)

    
    def loadLevel(self, score:int):
        self.score = score
        event_bus.publish("clean_queued_commands")
        event_bus.publish("add_surface_to_render", self.background, [1024/2, 640/2], 0, True)
        self.buttonFont = pygame.font.Font("assets/fonts/Gowun.ttf", 32)
        self.buttonRects.clear()
        event_bus.subscribe("mouse_up", self.onMouseUp)
        event_bus.publish("change_music", "assets/sounds/sneaky-end.mp3")
        event_bus.publish("play_sound", self.sound1)
        
        super().loadLevel()
    
    def update(self):
        self.buttonRects.clear()
        i = 1
        for item in self.menuItems:
            button = self.buttonFont.render(item["title"], True, (255,255,255,255))
            buttonPos = (64, 300 + 64 * i)
            # Stroke noir autour du texte
            for dx in [-2, 0, 2]:
                for dy in [-2, 0, 2]:
                    if dx != 0 or dy != 0:
                        stroke = self.buttonFont.render(item["title"], True, (0,0,0,255))
                        event_bus.publish(
                            "add_surface_to_render",
                            stroke,
                            [buttonPos[0] + button.get_size()[0]/2 + dx, buttonPos[1] + button.get_size()[1]/2 + dy],
                            10
                        )
            event_bus.publish(
                "add_surface_to_render",
                button,
                [buttonPos[0] + button.get_size()[0]/2, buttonPos[1] + button.get_size()[1]/2],
                10
            )
            rect = button.get_rect(topleft=buttonPos)
            self.buttonRects.append((rect, item["action"]))
            i += 1
    
    def onMouseUp(self, pos):
        for rect, action in self.buttonRects:
            if rect.collidepoint(pos):
                action()

    def unloadLevel(self):
        super().unloadLevel()
    
    def quitGame(self):
        command = QuitGameCommand()
        event_bus.publish("queue_command", command)
