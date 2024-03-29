import pygame
from menu import Menu
from game_controller import GameController

def main():
    pygame.init()
    game_controller = GameController(game_mode="human")
    screen = pygame.display.set_mode((960, 860))

    while True:
        start = game_controller.menuing()
        if start == "play":
            game_controller.run()



if __name__ == "__main__":
    main()
