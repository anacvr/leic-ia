# menu.py

import pygame
import sys
from button import Button
from game_controller import GameController

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
                        game_mode = self.play_menu()
                        game_controller = GameController(game_mode)
                        if game_mode == "human":
                            game_controller.run()
                        elif game_mode == "ai":
                            game_controller.run()
                        elif game_mode == "ai2":
                            game_controller.run()

                    if instr_button.checkForInput(menu_mouse_pos):
                        return "instr"

                    if quit_button.checkForInput(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
            
    def play_menu(self):
        while True:
            human_button, ai_button, ai_button2 = self.draw_play_menu()
            menu_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if human_button.checkForInput(menu_mouse_pos):
                        return "human"

                    if ai_button.checkForInput(menu_mouse_pos):
                        return "ai"

                    if ai_button2.checkForInput(menu_mouse_pos):
                        return "ai2"
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()

            pygame.display.update()
