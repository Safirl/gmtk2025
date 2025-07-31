import pygame
from game import Game
from levelLoader import LevelLoader

def main():
    try:
        game = Game()
        levelLoader = LevelLoader()
        
        game.run()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

main()