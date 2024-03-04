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
                    if self.view.blink == False:
                        self.view.blink = True
                        self.view.blink_piece(x, y)
                    else:
                        self.view.blink = False
                        self.view.blink_piece_pos = None
                        self.model.move_piece(x, y, player=1)

            self.model.ai_move()
            self.view.draw()