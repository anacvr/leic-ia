import pygame

class GameView:
    def __init__(self, model):
        self.model = model
        pygame.init()

        self.window_size = 860
        self.margin = 30

        self.window = pygame.display.set_mode((self.window_size, self.window_size))

        # Define the colors for the pieces
        self.colorPlayer = (0, 0, 0)
        self.colorOpponent = (255, 255, 255)
        self.piecesColors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
        self.piecesSizes = [20, 25, 30, 35]

        pygame.display.set_caption("Terrace Game (LEIC-IA Group 112)")

    def draw(self):
        # Fill the window with white
        self.window.fill((255, 255, 255))

        # Define 8 distinct, moderately saturated colors for the L-shapes
        colors = [(81, 203, 255),
                  (93, 173, 233),
                  (108, 149, 208),
                  (128, 126, 184),
                  (158, 131, 184),
                  (189, 122, 173),
                  (211, 105, 156),
                  (255, 79, 134)]

        # Draw the grid
        for i in range(8):
            for j in range(8):
                # Select color based on cell position to create L-shaped pattern
                color = colors[max(min(i, j), min(7-i, 7-j))]
                pygame.draw.rect(self.window, color, (self.margin + i*100, self.margin + j*100, 100, 100))

                # Draw border around each cell
                pygame.draw.rect(self.window, (0, 0, 0), (self.margin + i*100, self.margin + j*100, 100, 100), 1)

        # Draw a thicker border around the entire board
        pygame.draw.rect(self.window, (0, 0, 0), (self.margin, self.margin, 800, 800), 5)

        # Draw the pieces
        self.draw_pieces()

        # Update the display
        pygame.display.update()


    # Draw all the pieces on the board
    def draw_pieces(self):

        for i in range(8):
            for j in range(8):
                piece = self.model.grid[j][i]

                # Skip empty cells
                if piece == 0:
                    continue
                
                # Extract player and type from the piece value
                player = piece // 10
                type = piece % 10

                self.draw_piece(player, type, i, j)
                

    # Draw the specified piece
    def draw_piece(self, player, type, x, y):
        pos =  (self.margin + x*100 + 50, self.margin + y*100 + 50)

        if player == 1:
            pieceColor = self.colorPlayer
        else:
            pieceColor = self.colorOpponent

        borderColor = self.piecesColors[type-1]
        size = self.piecesSizes[type-1]

        pygame.draw.circle(self.window, borderColor, pos, size + 3)
        pygame.draw.circle(self.window, pieceColor, pos, size)
