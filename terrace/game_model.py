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

    # Get the piece at the given coordinates
    def get_piece(self, x, y):
        # Convert screen coordinates to grid coordinates
        grid_x, grid_y = x // 100, y // 100

        for piece in self.pieces:
            if piece.x == grid_x and piece.y == grid_y:
                return piece
            

    def is_cell_empty(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return False
        return True
    
    def is_cell_adjacent(self, x1, y1, x2, y2):
        if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
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

    # Check if the move is valid, and if so, move the piece
    def check_move(self, piece, x, y):

        # Case 1: The target cell is on the same platform and is empty
        if self.is_cell_on_same_platform(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y):
            piece.move(x, y)

        # Case 2: The target cell is adjacent and is empty
        elif self.is_cell_adjacent(piece.x, piece.y, x, y) and \
        self.is_cell_empty(x, y):
            piece.move(x, y)

        # Case 3: The target cell is on the same platform and contains a piece of the opposite player and is diagonal
        elif self.is_cell_on_same_platform(piece.x, piece.y, x, y) and \
        not self.is_cell_empty(x, y) and \
        self.is_cell_diagonal(piece.x, piece.y, x, y):
            self.capture_piece(self.get_piece(x, y))
            piece.move(x, y)

        else:
            pass

        # TODO: Check if the target cell contains a piece of the same player
            
        # TODO: Check if the target cell contains a piece of the opposite player and is diagonal
        # Then captures the piece and moves the piece to the target cell


    def capture_piece(self, piece):
        # TODO: Implement piece capture

        # self.pieces.remove(piece)
        # del piece

        pass

    def ai_move(self):
        # Add AI logic here
        
        # Get the next move from the AI
        move = self.ai.get_next_move()
        self.check_move(move[0], move[1], move[2])

        pass