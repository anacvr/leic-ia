# menu.py

import pygame
import sys
from button import Button
from game_controller import GameController
from game_view import GameView
from game_model import GameModel

class Menu:
    def __init__(self, screen, state_machine):
        self.screen = screen
        self.state_machine = state_machine
        self.model = GameModel()
        self.view = GameView(self.model)
        
        #Bakground image and font for menu
        self.bg = pygame.image.load("resources/terrace_bk.png")
        self.menu_font = pygame.font.Font("resources/font.ttf", 100)


    def main_menu(self):
        while True:
            play_button, instr_button, quit_button = self.view.draw_main_menu()
            menu_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        game_mode = self.play_menu()
                        game_controller = GameController(game_mode, self.state_machine)
                        if game_mode == "human":
                            game_controller.run()
                        elif game_mode == "ai":
                            game_controller.run()
                        elif game_mode == "ai2":
                            game_controller.run()

                    if instr_button.checkForInput(menu_mouse_pos):
                        self.Instructions()

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
            human_button, ai_button, ai_button2 = self.view.draw_play_menu()
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
    
    def Instructions(self):
        while True:
            mainmenu_button = self.view.draw_Inst()
            menu_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mainmenu_button.checkForInput(menu_mouse_pos):
                        return


            pygame.display.update()
            
            
            