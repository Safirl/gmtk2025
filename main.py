import pygame
from game import Game
from levelLoader import LevelLoader

def main():
    try:
        # Créer les composants
        game = Game()
        levelLoader = LevelLoader()  # Il s'enregistre automatiquement aux événements
        
        # Lancer le jeu
        game.run()
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()