from piece import Piece

class GameModel:
    def __init__(self):

        self.pieces = []
        self.board = [[0 for _ in range(8)] for _ in range(8)]

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


    def move_piece(self, x, y, player):
        # Convert screen coordinates to grid coordinates
        grid_x, grid_y = x // 100, y // 100

        # Erase the piece from its original position
        # self.grid[grid_x][grid_y] = 0
        
        # TODO: Implement the logic to move the piece to the new position
        pass 

    def ai_move(self):
        # Add AI logic here
        pass