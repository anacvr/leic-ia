from piece import Piece
from game_ai import GameAI

class GameModel:
    def __init__(self):

        self.pieces = []
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.ai = GameAI(self)

        # Create the pieces for both players
        for i in range(8):
            # smaller to bigger
            pieceType = int(i/2 % 4 + 1)

            self.pieces.append(Piece(2, i, 1, pieceType))
            self.pieces.append(Piece(1, i, 7, pieceType))
            
            # bigger to smaller
            pieceType = int((7-i)/2 % 4 + 1)
            
            self.pieces.append(Piece(2, i, 0, pieceType))
            self.pieces.append(Piece(1, i, 6, pieceType))

        # Create the platforms
        for i in range(8):
            for j in range(8):
                # Calculate the height of the platform based on its position

                # top left - WORKING
                if i < 4 and j < 4:
                    self.board[i][j] = min(7-i, 7-j)
                
                # bottom right - WORKING
                elif i >= 4 and j >= 4:
                    self.board[i][j] = min(i, j)

                # top right - NOT WORKING
                elif i < 4 and j >= 4:
                    self.board[i][j] = max(i, 7-j)

                # bottom left - WORKING
                else:
                    self.board[i][j] = max(7-i, j)



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
            else:
                if x1 < x2:
                    x1 += 1
                elif x1 > x2:
                    x1 -= 1
                if y1 < y2:
                    y1 += 1
                elif y1 > y2:
                    y1 -= 1

                if self.is_cell_empty(x1, y1):
                    continue
                else:
                    return (piece.player != player for piece in self.pieces if piece.x == x1 and piece.y == y1)
        
        return False

    # Check if the move is valid, and if so, moves the piece
    def check_move(self, piece, x, y):

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
        self.is_cell_empty(x, y): 
            piece.move(x, y)

        # Case 2: The target cell is above the current cell and is empty
        elif not self.is_cell_lower(piece.x, piece.y, x, y) and \
        (self.is_cell_adjacent(piece.x, piece.y, x, y) or self.is_cell_diagonally_adjacent(piece.x, piece.y, x, y)) and \
        self.is_cell_empty(x, y):
            piece.move(x, y)

        # Case 3: The target cell is below the current cell and is empty
        elif self.is_cell_lower(piece.x, piece.y, x, y) and \
        self.is_cell_adjacent(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y):
            piece.move(x, y)


        # CAPTURE
        # The target cell is diagonally adjacent and on a lower platform level
        # And the target cell contains an opponent's piece with a smaller or equal size
        elif self.is_cell_lower(piece.x, piece.y, x, y) and \
        self.is_cell_diagonally_adjacent(piece.x, piece.y, x, y) and \
        target_piece is not None and \
        target_piece.player != piece.player and \
        piece.size >= target_piece.size:
            piece.move(x, y)
            self.capture_piece(target_piece)

        ### DEBUGGING
        print("Is piece jumping over opponent?", self.is_jumping_over_opponent(piece.x, piece.y, x, y, piece.player))
        ###

        """ else:
            print("Invalid move")
            return False
        
        return True """
  

    def capture_piece(self, piece):
        if piece in self.pieces:
            self.pieces.remove(piece)
            del piece
        else:
            pass

    def is_game_over(self):
        """
        Check if the game is over.
        This function should return True if the game is over, False otherwise.
        """
        # TODO: Implement the logic to check if the game is over here
        # TODO: Check if there are no more valid moves for the current player

        for piece in self.pieces:
            # Case 1: The game is over if a T piece is eaten
            if piece.isTpiece and piece.player == 1:
                return False
            elif piece.isTpiece and piece.player == 2:
                return False
            
            # Case 2: The game is over if a T piece reaches the opposite end
            elif piece.isTpiece and piece.player == 1:
                if piece.x == 7 and piece.y == 0:
                    return True
            elif piece.isTpiece and piece.player == 2:
                if piece.x == 0 and piece.y == 7:
                    return True

    def ai_move(self):
        # Add AI logic here
        
        # Get the next move from the AI
        # move = self.ai.get_next_move()
        # self.check_move(move[0], move[1], move[2])

        pass