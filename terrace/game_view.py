import pygame

class GameView:
    def __init__(self, model):
        self.model = model
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Terrace Game (LEIC-IA Group 112)")

    def draw(self):
        # Fill the window with white
        self.window.fill((255, 255, 255))

        # Define 8 distinct, moderately saturated colors for the L-shapes
        colors = [(255, 79, 134), (211, 105, 156), (189, 122, 173), (158, 131, 184), (128, 126, 184), (108, 149, 208), (93, 173, 233), (81, 203, 255)]

        # Draw the grid
        for i in range(8):
            for j in range(8):
                # Select color based on cell position to create L-shaped pattern
                color = colors[max(min(i, j), min(7-i, 7-j))]
                pygame.draw.rect(self.window, color, (i*100, j*100, 100, 100))

                # Draw border around each cell
                pygame.draw.rect(self.window, (0, 0, 0), (i*100, j*100, 100, 100), 1)

        # Update the display
        pygame.display.update()