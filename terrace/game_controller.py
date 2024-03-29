import pygame
import sys
from game_model import GameModel
from game_view import GameView
from game_state import GameState
from menu import Menu

class GameController:
    def __init__(self, game_mode):
        self.model = GameModel()
        self.view = GameView(self.model)
        self.game_state = self.model.game_state
        self.menu = Menu(self.view.window)
        self.selected_piece = None
        self.pieces = self.model.pieces
        pygame.mixer.init()
        pygame.mixer.music.load("resources/victory.mp3")

        self.board_start = self.view.margin
        self.board_end_x = self.view.margin + self.view.board_width
        self.board_end_y = self.view.margin + self.view.board_height
        
        self.turn = 1
        self.game_mode = game_mode

    def quit_game(self):
        pygame.quit()
        sys.exit()
        
    def handle_event(self, event, turn):
        if event.type == pygame.QUIT:
            self.quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            return self.handle_click(x, y, turn)
        return True
    
    def handle_click(self, x, y, turn):
        # Check if the click is outside the board area
        if x < self.board_start or x > self.board_end_x or y < self.board_start or y > self.board_end_y:
            return True
 
        x, y = self.view.window_to_board_coords(x, y)

        # If no piece is selected, select the piece at the clicked position
        piece = self.model.get_piece(x, y)
        if self.selected_piece is None and piece is not None and self.turn == piece.player:
            self.view.blink = True
            self.view.blink_piece(x, y)
            self.selected_piece = piece
        else:
            return self.handle_move(self.selected_piece, x, y, turn)
        
        return True
    
    def handle_move(self, piece, x, y, turn):
        self.view.blink = False
        self.view.blink_piece_pos = None
        
        # Check if the move is valid
        if(self.model.check_move(piece, x, y)):
            
            # Check if the move is capturing an opponent's piece
            if self.model.is_capturing_move(piece, x, y):
                target_piece = self.model.get_piece(x, y)
                self.model.capture_piece(target_piece)
                del target_piece
            
            piece.move(x, y)
            
            self.turn = 2 if self.turn == 1 else 1
            
            # Check if the game is over
            game_over = self.check_game_over()
            self.selected_piece = None
            return game_over
        
        # Reset the selected piece
        self.selected_piece = None
        return True
    
    def check_game_over(self):
        state = GameModel.is_game_over(self)
        if(state == True):
            pygame.mixer.music.play(loops=-1)
            action = self.view.winnerPopUp("Congratulations!")
            if action == "play":
                self.reset_game()
                pygame.mixer.music.stop()
                self.run()
            else:
                self.reset_game()
                pygame.mixer.music.stop()
                self.menuing()
            return False
        return True

    def run(self):
        while True:
            if self.game_mode == "human":
                for event in pygame.event.get():
                    if not self.handle_event(event, self.turn):
                        return
            elif self.game_mode == "ai":
                if self.turn == 1:
                    for event in pygame.event.get():
                        if not self.handle_event(event, self.turn):
                            return
                else:
                    self.model.ai_move(2)
                    if not self.check_game_over():
                        return
                    self.turn = 1
            elif self.game_mode == "ai2":
                self.model.ai_move(self.turn)
                if not self.check_game_over():
                    return
                self.turn = 2 if self.turn == 1 else 1
            self.view.draw()
    
    def reset_game(self):
        self.model = GameModel()
        self.view = GameView(self.model)
        self.selected_piece = None
        self.pieces = self.model.pieces

 
    
    def menuing(self):
        action = self.main_menu()
        print (action)
        if action == "play":
            self.run()
        elif action == "instr":
            self.Instructions()

        
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
                        self.menuing()


            pygame.display.update()

    
    def main_menu(self):
        while True:
            play_button, instr_button, quit_button = self.menu.draw_main_menu()
            menu_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        game_mode = self.play_menu()
                        if game_mode == "human":
                            self.run()
                        elif game_mode == "ai":
                            self.run()
                        elif game_mode == "ai2":
                            self.run()

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
            
    def play_menu(self):
        while True:
            human_button, ai_button, ai_button2 = self.menu.draw_play_menu()
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
                        self.menu.main_menu()

            pygame.display.update()
