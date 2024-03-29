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
    
    # Create options for human vs human, human vs AI, and AI vs AI
    def draw_play_menu(self):
        self.screen.blit(self.bg, (0, 0))
        
        menu_text = self.menu_font.render("PLAY", True, "#1E2345")
        menu_rect = menu_text.get_rect(center=(480, 200))
        self.screen.blit(menu_text, menu_rect)

        #Buttons for human vs human, human vs AI, and AI vs AI
        human_button = Button(image=pygame.image.load("resources/instr_menu.png"), pos=(470, 350),
                             text_input="HUMAN VS HUMAN", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")
        ai_button = Button(image=pygame.image.load("resources/instr_menu.png"), pos=(470, 500),
                             text_input="HUMAN VS AI", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")
        ai_button2 = Button(image=pygame.image.load("resources/rect_menu.png"), pos=(470, 650),
                             text_input="AI VS AI", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")

        for button in [human_button, ai_button, ai_button2]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.screen)

        return human_button, ai_button, ai_button2


