# menu.py

import pygame
import sys
from button import Button

class Menu:
    def __init__(self, screen):
        self.screen = screen
        
        #Bakground image and font for menu
        self.bg = pygame.image.load("resources/terrace_bk.png")
        self.menu_font = pygame.font.Font("resources/font.ttf", 100)

    def draw_main_menu(self):
        self.screen.blit(self.bg, (0, 0))
        
        menu_text = self.menu_font.render("MAIN MENU", True, "#1E2345")
        menu_rect = menu_text.get_rect(center=(480, 200))
        self.screen.blit(menu_text, menu_rect)

        #Buttons for play, instructions, and quit
        play_button = Button(image=pygame.image.load("resources/rect_menu.png"), pos=(480, 350),
                             text_input="PLAY", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")
        instr_button = Button(image=pygame.image.load("resources/instr_menu.png"), pos=(480, 500),
                                text_input="INSTRUCTIONS", font=pygame.font.Font("resources/font.ttf", 75),
                                base_color="#85BEE4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("resources/rect_menu.png"), pos=(480, 650),
                             text_input="QUIT", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")

        for button in [play_button, instr_button, quit_button]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)

        return play_button, instr_button, quit_button


    def main_menu(self):
        while True:
            play_button, instr_button, quit_button = self.draw_main_menu()
            menu_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        return "play"
                    # TODO: Create different options to play the game

                    if instr_button.checkForInput(menu_mouse_pos):
                        return"instr"

                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

