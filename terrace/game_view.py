import pygame

class GameView:
    def __init__(self, model):
        self.model = model
        pygame.init()

        self.window_height = 860
        self.window_width = 960

        self.margin = 30

        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        self.board = pygame.Surface((800, 800))

        self.blink = False
        self.blink_piece_pos = None
        self.blink_start_time = None

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


    """ # Draw all the pieces on the board
    def draw_pieces(self):

        for i in range(8):
            for j in range(8):
                piece = self.model.grid[j][i]

                # Skip empty cells
                if piece == 0:
                    continue

                # Skip the blinking piece if it should not be drawn
                if (i, j) == self.blink_piece_pos and int((pygame.time.get_ticks() - self.blink_start_time) / 500) % 2 == 0:
                    continue
                
                # Extract player and type from the piece value
                player = piece // 10
                type = piece % 10

                self.piece.draw(self.window) """
    
    def draw_pieces(self):
        for piece in self.model.pieces:
            piece.draw(self.window)
                


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
        self.blink_piece_pos = (grid_x, grid_y)
        self.blink_start_time = pygame.time.get_ticks()