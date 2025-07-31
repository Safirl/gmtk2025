import os
import pygame
from pygame import Vector2, Rect, Surface
from eventBus import event_bus
from foot import Foot
import pytweening

os.environ['SDL_VIDEO_CENTERED'] = '1'

class RenderItem:
    """
    Classe pour stocker les informations de rendu
    """
    def __init__(self, surface: Surface, position, layer=0, isPersistent=False):
        self.surface = surface
        self.position = position 
        self.position[0] -= self.surface.get_width()/2
        self.position[1] -= self.surface.get_height()/2
        self.layer = layer
        self.isPersistent = isPersistent
        self.rect = Rect(position[0], position[1], surface.get_width(), surface.get_height())

class UserInterface():
    def __init__(self):
        self.worldSize = Vector2(1024, 640)
        self.window = pygame.display.set_mode(self.worldSize)
        pygame.display.set_caption("My game")
        
        self.renderQueue = []
        event_bus.subscribe("add_surface_to_render", self.addSurfaceToRender)
        event_bus.subscribe("clear_render_queue", self.clearRenderQueue)
        event_bus.subscribe("remove_surface", self.removeSurface)
        
        #animation
        self.progress = 0

    def render(self):
        self.window.fill((0, 0, 0))
        
        sorted_queue = sorted(self.renderQueue, key=lambda item: item.layer)
        
        for render_item in sorted_queue:
            try:
                self.window.blit(render_item.surface, render_item.position)
            except Exception as e:
                print(f"Error while rendering: {e}")
                
        self.clearRenderQueue()
        
        pygame.display.update()
        
    def addSurfaceToRender(self, surface, position, layer=0, isPersistent=False):
        """(progress) * 
        Args:
            surface: texture to draw
            position: x,y
            layer: the lower is closer to the background
        """
        render_item = RenderItem(surface, position, layer, isPersistent)
        self.renderQueue.append(render_item)
        # print(f"🎨 Surface ajoutée à la queue (position: {position}, layer: {layer})")
        
    def removeSurface(self, surface_id=None, position=None):
        if position:
            # Retirer par position
            self.renderQueue = [item for item in self.renderQueue 
                              if (item.position[0] != position[0] or item.position[1] != position[1])]
        else:
            print("Suppression Method unspecified")
    
    def clearRenderQueue(self, bForceCleaning=False):
        if bForceCleaning:
            self.renderQueue.clear()
            return
        self.renderQueue = list(filter(lambda item: item.isPersistent, self.renderQueue))
        # print("🧹 Queue de rendu vidée")
      
    #TODO  
    # def shakeCamera(self):
    #     if self.progress < 1.:
    #         self.isCameraShaking = True
    #     else:
    #         self.isCameraShaking = False
            
    #     value = pytweening.easeInElastic(self.progress) * 100
    #     for item in self.renderQueue:
    #         item.position[0] += value
    #         item.position[1] += value
    #     self.progress += .1
        

class Game():
    def __init__(self):
        pygame.init()
        self.ui = UserInterface()
        
        self.commands = []
        event_bus.subscribe("queue_command", self.queueCommand)
        event_bus.subscribe("start_game", self.startGame)
        
        self.clock = pygame.time.Clock()
        self.timer = 60. #in seconds
        self.running = True
        self.isGameRunning = False
    
    def queueCommand(self, newCommand):
        self.commands.append(newCommand)
        
    def startGame(self):
        self.isGameRunning = True
        foot = Foot("", "assets/foot.jpg", "assets/alpha/laces.png", "assets/laces/laces.png", "assets/shoesLevel/unhappy.png", "assets/shoesLevel/happy.png", True)
        
        self.loadLevel("shoes", foot)
        

    def processInput(self):
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                event_bus.publish('mouse_down', mousePos)
            elif event.type == pygame.MOUSEBUTTONUP:
                event_bus.publish('mouse_up', mousePos)
        
        event_bus.publish('mouse_moved', mousePos)

    def update(self):
        
        event_bus.publish('game_update')
        for command in self.commands:
            command.run()
        self.commands.clear()
        
        if not self.isGameRunning:
            return
        if self.clock.get_fps() != 0.:
            dt = self.clock.tick(60) / 1000.0
            self.timer -= dt

    def loadLevel(self, levelName, *args):
        event_bus.publish('load_level', levelName, *args)

    def run(self):
        # foot = Foot("", "assets/foot.jpg", "assets/alpha/laces.png", "assets/laces/laces.png", True)
        # self.loadLevel("shoes", foot)
        self.loadLevel("mainScreen")
        
        while self.running:
            self.processInput()
            self.update()
            self.ui.render()
            self.clock.tick(60)