import pygame
import sys
import time
from game_model import GameModel
from game_view import GameView

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = GameView(self.model)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    grid_x, grid_y = x // 100, y // 100
                    aux = self.model.grid[grid_x][grid_y]
                    while True:
                        self.view.draw()
                        time.sleep(2)
                        self.model.grid[grid_x][grid_y] = 0
                        self.view.draw()
                        self.model.grid[grid_x][grid_y] = aux
                    self.model.move_piece(x, y, player=1)

            self.model.ai_move()
            self.view.draw()