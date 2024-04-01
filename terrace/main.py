import pygame
from menu import Menu
from game_controller import GameController

class GameStateMachine:
    def __init__(self, screen):
        self.screen = screen
        self.current_state = "menu"
        self.menu = Menu(screen, self)
        self.game_controller = GameController("human", self, 2)

    def handle_event(self, event):
        if self.current_state == "menu":
            return self.menu.main_menu()
        elif self.current_state == "game":
            return self.game_controller.handle_event(event)

    def render(self):
        if self.current_state == "menu":
            self.menu.main_menu()
        elif self.current_state == "game":
            self.game_controller.view.draw()
    
    def change_state(self, new_state):
        self.current_state = new_state

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("resources/victory.mp3")

    screen = pygame.display.set_mode((960, 860))
    
    state_machine = GameStateMachine(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            next_state = state_machine.handle_event(event)
            if next_state:
                state_machine.change_state(next_state)

        state_machine.render()

        pygame.display.update()


if __name__ == "__main__":
    main()
