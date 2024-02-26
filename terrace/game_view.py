import pygame
import time

class GameView:
    def __init__(self, model):
        self.model = model
        pygame.init()

        self.window_height = 860
        self.window_width = 960
        self.margin = 30

        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        # Define the colors for the pieces
        self.colorPlayer = (0, 0, 0)
        self.colorOpponent = (255, 255, 255)
        self.piecesColors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
        self.piecesSizes = [20, 25, 30, 35]

        self.blink = False

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
        
        # Define the elevation levels for the border thickness
        elevation_levels = [1, 2, 3, 4, 5, 6, 7, 8]

        # Draw the grid
        for i in range(8):
            for j in range(8):
                # Select color based on cell position to create L-shaped pattern
                color = colors[max(min(i, j), min(7-i, 7-j))]
                pygame.draw.rect(self.window, color, (self.margin + i*100, self.margin + j*100, 100, 100))

                # Get the elevation level for the current cell
                elevation = elevation_levels[max(min(i, j), min(7-i, 7-j))]

                # Draw border around each cell with variable thickness based on elevation
                pygame.draw.rect(self.window, (0, 0, 0), (self.margin + i*100, self.margin + j*100, 100, 100), elevation)

        # Draw a thicker border around the entire board
        pygame.draw.rect(self.window, (0, 0, 0), (self.margin, self.margin, 800, 800), 5)

        # Draw the pieces
        self.draw_pieces()
        
        self.draw_legend()

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


    def draw_legend(self):
        #define font and legend
        legend_font = pygame.font.Font(None, 20)
        legend_text = legend_font.render("Legend:", True, (0, 0, 0))
        
        #renders the legend text onto the game window
        self.window.blit(legend_text, (self.window_width - 100, 50))
        
        #for each color, draw a rectangle and a text label
        for i, color in enumerate([(81, 203, 255), (93, 173, 233), (108, 149, 208), (128, 126, 184), (158, 131, 184), (189, 122, 173), (211, 105, 156), (255, 79, 134)]):
            pygame.draw.rect(self.window, color, (self.window_width - 40, 80 + i*40, 30, 30))
            text = legend_font.render(f"Step {i+1}", True, (0, 0, 0))  #F-strings to format the string the right way
            self.window.blit(text, (self.window_width - 100, 80 + i*40))

    def blink_piece(self, x, y):
        grid_x, grid_y = x // 100, y // 100
        aux = self.model.grid[grid_y][grid_x]
        while self.blink == True:
            self.model.grid[grid_y][grid_x] = 0
            self.draw()
            time.sleep(0.5)
            self.model.grid[grid_y][grid_x] = aux
            self.draw()
            time.sleep(0.5)