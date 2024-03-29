import pygame
import sys
from game_model import GameModel
from game_view import GameView
from game_state import GameState
from menu import Menu

class GameController:
    def __init__(self):
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
        

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            if(self.turn == 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit_game()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return
                        
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()

                        # Check if the click is outside the board area
                        if x < self.board_start or x > self.board_end_x or y < self.board_start or y > self.board_end_y:
                            continue
                        
                        else:
                            x, y = self.view.window_to_board_coords(x, y)

                            # If no piece is selected, select the piece at the clicked position
                            if self.selected_piece is None:
                                self.view.blink = True
                                self.view.blink_piece(x, y)
                                self.selected_piece = self.model.get_piece(x, y)

                            # If a piece is selected, check move with clicked position
                            else:
                                self.view.blink = False
                                self.view.blink_piece_pos = None

                                # Check if the move is valid
                                if(self.model.check_move(self.selected_piece, x, y)):
                                    
                                    self.selected_piece.move(x, y)

                                    # Check if the move is capturing an opponent's piece
                                    if self.model.is_capturing_move(self.selected_piece, x, y):
                                        target_piece = self.model.get_piece(x, y)
                                        self.model.capture_piece(target_piece)
                                        del target_piece
                                
                                # Check if the game is over
                                playerWon = False
                            state = GameModel.is_game_over(self, playerWon)

                            if(state == True):
                                if (playerWon == False):
                                    pygame.mixer.music.play(loops=-1)
                                    action = self.view.winnerPopUp("Player 1 Wins")
                                    if action == "play":
                                        self.reset_game()
                                        pygame.mixer.music.stop()
                                        self.run()
                                    else:
                                        self.reset_game()
                                        pygame.mixer.music.stop()
                                        self.menuing()
                                        pass

                                if (playerWon == True):
                                    pygame.mixer.music.play(loops=-1)
                                    action = self.view.winnerPopUp("Player 2 Wins")
                                    if action == "play":
                                        self.reset_game()
                                        self.run()
                                    else:
                                        self.reset_game()
                                        self.menuing()
                                        
                                        pass
                                    
                                # Reset the selected piece
                                self.selected_piece = None

                                # Change the turn
                                self.turn = 2

            elif(self.turn == 2):
                # AI move
                self.model.ai_move(2)

                # Check if the game is over
                playerWon = False
                state = GameModel.is_game_over(self, playerWon)

                if(state == True):
                    self.quit_game()
            
                self.turn = 1

            
            self.view.draw()
    
    def reset_game(self):
        self.model = GameModel()
        self.view = GameView(self.model)
        self.selected_piece = None
        self.pieces = self.model.pieces

 
    
    def menuing(self):
        action = self.menu.main_menu()
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
