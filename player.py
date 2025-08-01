import pygame
from eventBus import event_bus

class Player():
    def __init__(self):
       
        self.sprite = pygame.image.load("assets/handStreetPlayer.png")
        self.x = 400  
        self.y = 550 
        
       
        self.width = 50  
        self.height = 50
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        
        event_bus.subscribe('mouse_moved', self.follow_mouse)

    def follow_mouse(self, mouse_pos):
        
        self.x = mouse_pos[0] 
        self.x = max(0, min(self.x, 1024 - self.width))
        self.rect.x = self.x


    def update(self):
        event_bus.publish(
            "add_surface_to_render",
            self.sprite,
            [self.x, self.y],
            2 
        )
    def check_collision(self, foot_rect):
        return self.rect.colliderect(foot_rect)