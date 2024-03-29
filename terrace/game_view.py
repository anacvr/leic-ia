import pygame
from button import Button

class GameView:
    def __init__(self, model):
        self.model = model
        self.bg = pygame.image.load("resources/terrace_bk.png")
        self.menu_font = pygame.font.Font("resources/font.ttf", 100)
        pygame.init()

        self.window_height = 860
        self.window_width = 960

        self.board_height = 800
        self.board_width = 800

        self.margin = 30

        self.window = pygame.display.set_mode((self.window_width, self.window_height))

        self.board = self.model.board

        self.blink = False
        self.blink_piece_pos = None
        self.blink_start_time = None

        pygame.display.set_caption("Terrace (LEIC-IA Group 112)")
    
    def window_to_board_coords(self, x, y):
        """
        Convert window coordinates to board coordinates.
        """
        return (x - self.margin) // 100, (y - self.margin) // 100

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
                color = colors[self.model.board[i][j]]
                pygame.draw.rect(self.window, color, (self.margin + i*100, self.margin + j*100, 100, 100))

                # Get the elevation level for the current cell
                elevation = self.model.board[i][j] + 1

                # Draw border around each cell with variable thickness based on elevation
                pygame.draw.rect(self.window, (0, 0, 0), (self.margin + i*100, self.margin + j*100, 100, 100), elevation)

        # Draw a thicker border around the entire board
        pygame.draw.rect(self.window, (0, 0, 0), (self.margin, self.margin, self.board_height, self.board_width), 5)

        # Draw the pieces
        self.draw_pieces()
        
        # Draw the legend
        self.draw_legend()

        # Update the display
        pygame.display.update()

    
    def draw_pieces(self):
        current_time = pygame.time.get_ticks()
        for piece in self.model.pieces:
            if (piece.x, piece.y) == self.blink_piece_pos and self.blink and (current_time - self.blink_start_time) % 1000 < 500:
                continue
            piece.draw(self.window)
    

    def draw_legend(self):
        # Define font and legend
        legend_font = pygame.font.Font(None, 20)
        legend_text = legend_font.render("Legend:", True, (0, 0, 0))
        
        # Renders the legend text onto the game window
        self.window.blit(legend_text, (self.window_width - 100, 50))
        
        # For each color, draw a rectangle and a text label
        for i, color in enumerate([(81, 203, 255), (93, 173, 233), (108, 149, 208), (128, 126, 184), (158, 131, 184), (189, 122, 173), (211, 105, 156), (255, 79, 134)]):
            pygame.draw.rect(self.window, color, (self.window_width - 40, 80 + i*40, 30, 30))
            text = legend_font.render(f"Step {i+1}", True, (0, 0, 0))  #F-strings to format the string the right way
            self.window.blit(text, (self.window_width - 100, 80 + i*40))

    def blink_piece(self, x, y):
        self.blink_piece_pos = (x, y)
        self.blink_start_time = pygame.time.get_ticks()

    def draw_victory(self, winner):
        
        menu_text = self.menu_font.render( winner, True, "#1E2345")
        menu_rect = menu_text.get_rect(center=(480, 200))
        self.window.blit(menu_text, menu_rect)

        play_button = Button(image=pygame.image.load("resources/rect_menu.png"), pos=(480, 350),
                             text_input="PLAY AGAIN", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")
        mainmenu_button = Button(image=pygame.image.load("resources/rect_menu.png"), pos=(480, 650),
                             text_input="MAIN MENU", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")

        for button in [play_button, mainmenu_button]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.window)

        return play_button, mainmenu_button
    
    def winnerPopUp(self, winner):
        while True:
            play_button, mainmenu_button = self.draw_victory(winner)
            menu_mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.checkForInput(menu_mouse_pos):
                        return "play"

                    if mainmenu_button.checkForInput(menu_mouse_pos):
                        return "menu"


            pygame.display.update()


    def draw_Inst(self):
        self.window.blit(self.bg, (0, 0))
        menu_text = self.menu_font.render("TERRACE RULES", True, "#1E2345")
        menu_rect = menu_text.get_rect(center=(480, 200))
        self.window.blit(menu_text, menu_rect)
        
            # Rules
        rule_font = pygame.font.Font("resources/font.ttf", 30)
        rule_texts = [
            "1. Objective: Remove all your pieces from the board first.",
            " ",
            "2. Setup: Each player has 15 pieces of one color.",
            " ",
            "3. Gameplay: Move pieces to adjacent or higher level spaces." ,
            "You can move anywhere on the same level but only to ",
            "adjacent places when moving up or down a level.",
            " ",
            "4. Capturing: Capture opponent's pieces by moving onto them.",
            "You need to be in a higher lever and have a piece ",
            "of greater size.",
            " ",
            "5. Winning: Capture the Opponents T pice or have your ",
            "T piece reach the opponents T piece spawn point.",
            " ",
        ]
        y_offset = 300
        x_marginL = 40
        for text in rule_texts:
            rule_text_render = rule_font.render(text, True, "#FFFFFF")
            rule_text_rect = rule_text_render.get_rect(midleft=(x_marginL, y_offset))
            self.window.blit(rule_text_render, rule_text_rect)
            y_offset += 30
        mainmenu_button = Button(image=pygame.image.load("resources/rect_menu.png"), pos=(480, 780),
                             text_input="MAIN MENU", font=pygame.font.Font("resources/font.ttf", 75),
                             base_color="#85BEE4", hovering_color="White")

        for button in [mainmenu_button]:
            button.changeColor(pygame.mouse.get_pos())
            button.update(self.window)

        return mainmenu_button