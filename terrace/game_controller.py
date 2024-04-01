import pygame
import sys
from game_model import GameModel
from game_view import GameView

class GameController:
    def __init__(self, game_mode, state_machine, depth):
        self.model = GameModel(depth)
        self.view = GameView(self.model)
        self.game_state = self.model.game_state
        self.selected_piece = None
        self.pieces = self.model.pieces
        self.state_machine = state_machine


        self.board_start = self.view.margin
        self.board_end_x = self.view.margin + self.view.board_width
        self.board_end_y = self.view.margin + self.view.board_height
        
        self.turn = 1
        self.game_mode = game_mode

    def quit_game(self):
        pygame.quit()
        sys.exit()
        
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.quit_game()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state_machine.change_state("menu")
                return False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            return self.handle_click(x, y)
        
        return "game"
    
    def handle_click(self, x, y):
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
            return self.handle_move(self.selected_piece, x, y)
        
        return True
    
    def handle_move(self, piece, x, y):
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
            self.view.draw(self.turn)
            game_over = self.check_game_over()
            self.selected_piece = None
            return game_over
        
        # Reset the selected piece
        self.selected_piece = None
        return True
    
    def print_results_to_console(self, winner):
        print("\nFINAL STATISTICS:\n")
        print("Winner: ", winner)
        print("Player 1 moves: ", self.model.ai.turn_count_1)
        print("Player 2 moves: ", self.model.ai.turn_count_2)
    
    def check_game_over(self):
        winner = self.model.is_game_over(self.game_state)
        if winner is not None:
            self.print_results_to_console(winner)
            
            pygame.mixer.music.play(loops=-1)
            action = self.view.winnerPopUp(winner)

            if action == "play":
                self.reset_game()
                pygame.mixer.music.stop()
                self.run()
            else:
                self.reset_game()
                pygame.mixer.music.stop()
                self.state_machine.change_state("menu")
            return False
        return True

    def run(self):
        while True:
            if self.game_mode == "human":
                for event in pygame.event.get():
                    if not self.handle_event(event):
                        return
                    
            elif self.game_mode == "ai":
                if self.turn == 1:
                    for event in pygame.event.get():
                        if not self.handle_event(event):
                            return
                else:
                    self.model.ai_move(2)
                    self.view.draw(self.turn)
                    if not self.check_game_over():
                        return
                    self.turn = 1

            elif self.game_mode == "ai2":
                self.model.ai_move(self.turn)
                self.view.draw(self.turn)
                if not self.check_game_over():
                    return
                self.turn = 2 if self.turn == 1 else 1

            self.view.draw(self.turn)
    
    def reset_game(self):
        self.model = GameModel(self.model.depth)
        self.view = GameView(self.model)
        self.selected_piece = None
        self.game_state = self.model.game_state
        self.pieces = self.model.pieces
