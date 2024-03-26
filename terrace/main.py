import pygame
from game_controller import GameController
from menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((960, 860))

    menu = Menu(screen)
    game_controller = GameController(game_mode="human")

    while True:
        action = menu.main_menu()

        if action == "play":
            game_controller.run()
        elif action == "instr":
            pass

if __name__ == "__main__":
    main()
