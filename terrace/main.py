import pygame
from menu import Menu
from game_controller import GameController

def main():
    pygame.init()
    game_controller = GameController()
    screen = pygame.display.set_mode((960, 860))

    menu = Menu(screen)
    while True:
        start = game_controller.menuing()
        if start == "play":
            game_controller.run()



if __name__ == "__main__":
    main()
