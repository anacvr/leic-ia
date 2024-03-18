import pygame
import sys
from game_model import GameModel
from game_view import GameView

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = GameView(self.model)
        self.selected_piece = None
        self.pieces = self.model.pieces

        self.board_start = self.view.margin
        self.board_end_x = self.view.margin + self.view.board_width
        self.board_end_y = self.view.margin + self.view.board_height
        

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
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
                            self.model.check_move(self.selected_piece, x, y)
                            self.selected_piece = None

                            # Check if the game is over
                            playerWon = False
                            state = GameModel.is_game_over(self, playerWon)

                            if(state == True):
                                if (playerWon == False):
                                    print ("player 1 Wins")
                                    self.quit_game()
                                if (playerWon == True):
                                    print ("player 2 Wins")
                                    self.quit_game()

                            # AI move
                            self.model.ai_move()

                            # Check if the game is over
                            playerWon = False
                            state = GameModel.is_game_over(self, playerWon)

                            if(state == True):
                                self.quit_game()

            self.view.draw()