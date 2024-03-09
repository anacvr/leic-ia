import pygame
import sys
from game_model import GameModel
from game_view import GameView

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = GameView(self.model)
        self.selected_piece = None

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.view.blink == False:
                        self.view.blink = True
                        self.view.blink_piece(x, y)
                        self.selected_piece = self.model.get_piece(x, y)
                    else:
                        self.view.blink = False
                        self.view.blink_piece_pos = None
                        self.model.check_move(self.selected_piece, x, y)

            self.model.ai_move()
            self.view.draw()