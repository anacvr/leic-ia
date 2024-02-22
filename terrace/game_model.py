class GameModel:
    def __init__(self):

        # Create an 8x8 grid to represent the game board
        # And initialize it with the starting position of the pieces
        # 0: empty cell; 1x: player piece; 2x: opponent piece; x: piece size
        self.grid = [[24, 24, 23, 23, 22, 22, 21, 21],
                     [21, 21, 22, 22, 23, 23, 24, 24],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [14, 14, 13, 13, 12, 12, 11, 11],
                     [11, 11, 12, 12, 13, 13, 14, 14]]

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