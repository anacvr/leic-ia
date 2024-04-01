import pygame

class Piece:
    def __init__(self, player, x, y, type):
        self.player = player
        self.type = type
        self.x = x
        self.y = y

        self.prev_x = None
        self.prev_y = None

        self.isTpiece = False

        self.margin = 30

        # Check if the piece is a T piece
        if self.type == 1 and (self.x == 0 or self.x == 7) and (self.y == 0 or self.y == 7):
            self.isTpiece = True
            self.type = 1

        # Piece border colors and sizes for each type
        self.piecesColors = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0)]
        self.piecesSizes = [20, 25, 30, 35]

        # Piece color according to player
        if player == 1:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)

        # Set the border color and size for the piece
        self.borderColor = self.piecesColors[type-1]
        self.size = self.piecesSizes[type-1]

        # Load the T images for the special pieces
        self.imt_black = pygame.image.load('resources/t-black.png')
        self.imt_black = pygame.transform.scale(self.imt_black, (50, 50))
        
        self.imt_white = pygame.image.load('resources/t-white.png')
        self.imt_white = pygame.transform.scale(self.imt_white, (50, 50))

    def __str__(self):
        return f"Piece(player={self.player}, type={self.type}, x={self.x}, y={self.y})"  

    def draw(self, window):
        
        pos =  (self.margin + self.x*100 + 50, self.margin + self.y*100 + 50)

        pygame.draw.circle(window, self.borderColor, pos, self.size + 3)
        pygame.draw.circle(window, self.color, pos, self.size)
        
        # White piece - black T
        if self.isTpiece and self.player == 2:
            window.blit(self.imt_black, (pos[0] - self.imt_black.get_width() // 2, pos[1] - self.imt_black.get_height() // 2))

        # Black piece - white T
        if self.isTpiece and self.player == 1:
            window.blit(self.imt_white, (pos[0] - self.imt_white.get_width() // 2, pos[1] - self.imt_white.get_height() // 2))


    def move(self, x, y):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x
        self.y = y
        
    def return_to_prev_position(self):
        if self.prev_x is None or self.prev_y is None:
            return
        
        self.x = self.prev_x
        self.y = self.prev_y
        self.prev_x = None
        self.prev_y = None
        