import pygame

class Piece:
    def __init__(self, player, x, y, type):
        self.player = player
        self.type = type
        self.x = x
        self.y = y
        self.margin = 30

        self.piecesColors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
        self.piecesSizes = [20, 25, 30, 35]

        if player == 1:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

        self.borderColor = self.piecesColors[type-1]
        self.size = self.piecesSizes[type-1]

        

    def draw(self, window):
        pos =  (self.margin + self.x*100 + 50, self.margin + self.y*100 + 50)

        pygame.draw.circle(window, self.borderColor, pos, self.size + 3)
        pygame.draw.circle(window, self.color, pos, self.size)

