from game_ai import GameAI
from game_state import GameState
import time

class GameModel:
    def __init__(self, depth):
        self.game_state = GameState(self)
        self.pieces = self.game_state.pieces
        self.board = self.game_state.board
        self.depth = depth
        self.ai = GameAI(self, depth)

    # Get the piece at the given board coordinates
    def get_piece(self, x, y):

        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
    
    # Check what quadrant the piece is in
    def get_quadrant(self, x, y):
        if x < 4 and y < 4:
            return 1
        elif x >= 4 and y < 4:
            return 2
        elif x < 4 and y >= 4:
            return 3
        else:
            return 4

    def is_cell_empty(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return False
        return True
    
    # PROBABLY SHOULD BE MOVED TO THE PIECE CLASS
    def is_cell_on_same_platform(self, x1, y1, x2, y2):
        if self.board[x1][y1] == self.board[x2][y2]:
            return True
        return False
    
    # PROBABLY SHOULD BE MOVED TO THE PIECE CLASS
    def is_cell_lower(self, x1, y1, x2, y2):
        """Check if the cell (x2, y2) is lower than the cell (x1, y1)"""

        if self.board[x1][y1] > self.board[x2][y2]:
            return True
        return False
    
    def is_cell_on_same_quadrant(self, x1, y1, x2, y2):
        if self.get_quadrant(x1, y1) == self.get_quadrant(x2, y2):
            return True
        return False

    # PROBABLY SHOULD BE MOVED TO THE PIECE CLASS
    # Only considers the 4 adjacent cells (up, down, left, right)
    def is_cell_adjacent(self, x1, y1, x2, y2):
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        return False
    
    # PROBABLY SHOULD BE MOVED TO THE PIECE CLASS
    def is_cell_diagonally_adjacent(self, x1, y1, x2, y2):
        if abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
            return True
        return False
    
    def is_opponent_piece_on_same_platform(self, x, y, player):
        """Check if there is an opponent's piece on the same platform as the given cell (x, y)"""
        for piece in self.pieces:
            if self.board[piece.x][piece.y] == self.board[x][y] and \
            self.is_cell_on_same_quadrant(x, y, piece.x, piece.y) and \
            piece.player != player:
                return True
        return False
    
    def is_jumping_over_opponent(self, x1, y1, x2, y2, player):
        """Check if a piece is jumping over an opponent's piece on the same platform.
        x1, y1: Starting position
        x2, y2: Ending position
        player: Current player"""

        if not self.is_opponent_piece_on_same_platform(x1, y1, player):
            return False

        for i in range(7):
            if x1 == x2 and y1 == y2:
                break
            # TODO: This might be a problem with different quadrants at the same height
            else:
                if x1 < x2 and self.board[x1][y1] == self.board[x1+1][y1]:
                    x1 += 1
                elif x1 > x2 and self.board[x1][y1] == self.board[x1-1][y1]:
                    x1 -= 1
                if y1 < y2 and self.board[x1][y1] == self.board[x1][y1+1]:
                    y1 += 1
                elif y1 > y2 and self.board[x1][y1] == self.board[x1][y1-1]:
                    y1 -= 1

                # Check if the cell contains an opponent's piece
                if not self.is_cell_empty(x1, y1) and (piece.player != player for piece in self.pieces if piece.x == x1 and piece.y == y1) :
                    # print("Invalid Move: Jumping over opponent!")
                    return True
        
        return False


    def check_move(self, piece, x, y):
        """
        Check if the move is valid.
        piece: The piece to move
        x, y: The new position
        return: (is_valid, is_capturing)
            is_valid: True if the move is valid, False otherwise
            is_capturing: True if the move is capturing an opponent's piece, False otherwise
        """

        # Check if the clicked cell contains a piece
        if piece is None:
            return False
    
        target_piece = self.get_piece(x, y)

        # CANNIBALISM
        # The target cell contains a piece of the same player
        if target_piece is not None and target_piece.player == piece.player:
            return False


        # MOVEMENT
        # Case 1: The target cell is on the same platform and is empty
        elif self.is_cell_on_same_platform(piece.x, piece.y, x, y) and \
        self.is_cell_on_same_quadrant(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y) and \
        not self.is_jumping_over_opponent(piece.x, piece.y, x, y, piece.player): 
            return True

        # Case 2: The target cell is above the current cell and is empty
        elif not self.is_cell_lower(piece.x, piece.y, x, y) and \
        not self.is_cell_on_same_platform(piece.x, piece.y, x, y) and \
        (self.is_cell_adjacent(piece.x, piece.y, x, y) or self.is_cell_diagonally_adjacent(piece.x, piece.y, x, y)) and \
        self.is_cell_empty(x, y):
            return True

        # Case 3: The target cell is below the current cell and is empty
        elif self.is_cell_lower(piece.x, piece.y, x, y) and \
        self.is_cell_adjacent(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y):
            return True


        # CAPTURE
        # The target cell is diagonally adjacent and on a lower platform level
        # And the target cell contains an opponent's piece with a smaller or equal size
        elif self.is_capturing_move(piece, x, y):
            return True


        else:
            # print("Invalid move")
            return False
    

    def is_capturing_move(self, piece, x, y):
        """
        Check if the move is capturing an opponent's piece.
        piece: The piece to move
        x, y: The new position
        return: True if the move is capturing, False otherwise
        """

        target_piece = self.get_piece(x, y)

        if self.is_cell_lower(piece.x, piece.y, x, y) and \
        self.is_cell_diagonally_adjacent(piece.x, piece.y, x, y) and \
        target_piece is not None and \
        target_piece.player != piece.player and \
        piece.size >= target_piece.size:
            return True

        else: return False

    def capture_piece(self, piece):
        if piece in self.pieces:
            #print("A piece from Player ", piece.player, " was captured!")
            self.pieces.remove(piece)

    
    def uncapture_piece(self, piece):
        """
        Restore a captured piece.
        piece: The piece to restore
        """
        # Add the piece back to the game
        self.pieces.append(piece)
    
    def is_game_over(self, game_state):
        """
        Check if the game is over.
        This function should return the winning player's number if the game is over, None otherwise.
        """

        # Case 1: The game is over if a T piece is eaten
        # Assume both T pieces are dead
        t1dead = True 
        t2dead = True

        # Check if the T pieces are still in the game
        for piece in game_state.pieces:
            if piece.isTpiece and piece.player == 1:
                t1dead = False

            elif piece.isTpiece and piece.player == 2:
                t2dead = False

        if t1dead == True:
            # Player 2 wins because Player 1's T piece is eaten
            return 2
        elif t2dead == True:
            # Player 1 wins because Player 2's T piece is eaten
            return 1

        # Case 2: The game is over if a T piece reaches the opposite end
        for piece in game_state.pieces:
            if piece.isTpiece and piece.player == 1:
                if piece.x == 7 and piece.y == 0:
                    # Player 1 wins because their T piece reached the opposite end
                    return 1

            elif piece.isTpiece and piece.player == 2:
                if piece.x == 0 and piece.y == 7:
                    # Player 2 wins because their T piece reached the opposite end
                    return 2

        # The game is not over
        return None
                
                
    def ai_move(self, player):
        # Begin the timer
        start_time = time.time()

        best_move = self.ai.get_best_move(self.game_state, self.depth, player)

        # End the timer
        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        print(f"Time taken (ms) AI{player}: {elapsed_time_ms:.3f}")

        if best_move is not None:
            piece, (x, y) = best_move
            # Check if the move is a capturing move
            if self.is_capturing_move(piece, x, y):
                # If it is, capture the piece at the target location
                target_piece = self.get_piece(x, y)
                self.capture_piece(target_piece)
            # Then move the piece
            piece.move(x, y)

            # Increment the turn count
            self.increment_turn_count(player)
        else:
            print("AI has no valid moves!")


    def increment_turn_count(self, player):
        if player == 1:
            self.ai.turn_count_1 += 1
        else:
            self.ai.turn_count_2 += 1