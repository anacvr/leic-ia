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

        # Define 8 tones of gray
        colors = [(64 + i*16, 64 + i*16, 64 + i*16) for i in range(8)]

        # Draw the grid
        for i in range(8):
            for j in range(8):
                # Select color based on cell position to create L-shaped pattern
                color = colors[max(min(i, j), min(7-i, 7-j))]
                pygame.draw.rect(self.window, color, (i*100, j*100, 100, 100))

                # Draw border around each cell
                pygame.draw.rect(self.window, (255, 255, 255), (i*100, j*100, 100, 100), 1)

        # Draw thicker border around each L-level
        for i in range(4):
            pygame.draw.rect(self.window, (255, 255, 255), (i*100, i*100, (8-2*i)*100, (8-2*i)*100), 3)
            pygame.draw.rect(self.window, (255, 255, 255), ((7-i)*100, (7-i)*100, (8-2*i)*100, (8-2*i)*100), 3)

        # Update the display
        pygame.display.update()

        ### This is the code right now, but i still don't like it. You need to create L levels from each diagonal and they will meet at the center. But it needs to be better because right now it is still very against accssessibility :