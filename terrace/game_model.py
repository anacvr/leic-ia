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
            

    def is_cell_empty(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return False
        return True
    
    #only considers the moves straight up, down, left and right not diagonal
    def is_cell_adjacent(self, x1, y1, x2, y2):
        if (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
            return True
        return False
    
    def is_cell_on_same_platform(self, x1, y1, x2, y2):
        if self.board[x1][y1] == self.board[x2][y2]:
            return True
        return False
    
    def is_cell_diagonal(self, x1, y1, x2, y2):
        if abs(x1 - x2) == abs(y1 - y2):
            return True
        return False
    

    def is_cell_diagonal_low(self, x1, y1, x2, y2):
        if self.is_cell_diagonal(x1, y1, x2, y2) and self.board[x1][y1] > self.board[x2][y2]:
            return True
        return False
    """
    def is_path_clear(self, x1, y1, x2, y2):
        # Vertical movement
        if x1 == x2: 
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                if self.get_piece(x1, y) is not None:
                        return False
        # Horizontal movement
        elif y1 == y2:
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                if self.get_piece(x, y1) is not None:
                        return False
        # Diagonal movement
        elif abs(x1 - x2) == abs(y1 - y2):
            x_direction = 1 if x1 < x2 else -1
            y_direction = 1 if y1 < y2 else -1

            current_x, current_y = x1, y1
            while current_x != x2 or current_y != y2:
                current_x += x_direction
                current_y += y_direction
                if self.get_piece(current_x, current_y):
                        return False
                
        return True
    """

    # Check if the move is valid, and if so, move the piece
    def check_move(self, piece, x, y):
      
        target_piece = self.get_piece(x, y)
        
        if piece is None:
            return False
        
        # Case 1: The target cell contains a piece of the same player
        if target_piece is not None and target_piece.player == piece.player:
            return False

        # Case 2: The target cell is on the same platform and is empty
        elif self.is_cell_on_same_platform(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y):
            piece.move(x, y)

        # Case 3: The target cell is adjacent and is empty
        elif self.is_cell_adjacent(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y):
            piece.move(x, y)
 
        # Case 4: The target cell is diagonally adjacent and at a different platform level
        elif self.is_cell_diagonal(piece.x, piece.y, x, y):
            # Disallow moves that cross the center of the board
            if (piece.x - 3.5) * (x - 3.5) < 0 and (piece.y - 3.5) * (y - 3.5) < 0:
                return False
            
             # If the target cell is at a lower platform level and the piece is at a higher platform level, the move is only allowed if there is an opponent's piece at the target cell
            if self.is_cell_diagonal_low(piece.x, piece.y, x, y) and \
            target_piece is not None and \
            target_piece.player != piece.player and \
            piece.size >= target_piece.size:
                piece.move(x, y)
                self.capture_piece(target_piece)
                
            # If the target cell is at a higher platform level, the move is allowed
            elif self.board[piece.x][piece.y] < self.board[x][y] and target_piece is None:
                piece.move(x, y)
  

    def capture_piece(self, piece):
        if piece in self.pieces:
            self.pieces.remove(piece)
            del piece
        else:
            pass

    def ai_move(self):
        # Add AI logic here
        
        # Get the next move from the AI
        move = self.ai.get_next_move()
        self.check_move(move[0], move[1], move[2])

        pass