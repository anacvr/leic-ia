import pygame
import sys
from game_model import GameModel
from game_view import GameView
from game_state import GameState

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = GameView(self.model)
        self.game_state = self.model.game_state
        self.selected_piece = None
        self.pieces = self.model.pieces

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
                                state = GameModel.is_game_over(self)

                                if(state == True):
                                    self.quit_game()
                                    
                                # Reset the selected piece
                                self.selected_piece = None

                                # Change the turn
                                self.turn = 2

            elif(self.turn == 2):
                # AI move
                self.model.ai_move(2)

                # Check if the game is over
                state = GameModel.is_game_over(self)

                if(state == True):
                    self.quit_game()
            
                self.turn = 1

            
            self.view.draw()