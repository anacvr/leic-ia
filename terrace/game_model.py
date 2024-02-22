class GameModel:
    def __init__(self):
        # Create an 8x8 grid to represent the game board
        self.grid = [[0 for _ in range(8)] for _ in range(8)]

        # Initialize the pieces
        for i in range(8):
            self.grid[i][0] = 2  # Opponent's pieces
            self.grid[i][1] = 2  # Opponent's pieces

            self.grid[i][6] = 1  # Player's pieces
            self.grid[i][7] = 1  # Player's pieces

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