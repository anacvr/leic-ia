from piece import Piece

class GameState:
    def __init__(self, game_model):
        self.model = game_model
        self.pieces = []
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.captured_pieces = []
        self.moves_history = []

        # Create the pieces for both players
        for i in range(8):
            # smaller to bigger
            pieceType = int(i/2 % 4 + 1)

            self.pieces.append(Piece(2, i, 1, pieceType))
            self.pieces.append(Piece(1, i, 7, pieceType))
            
            # bigger to smaller
            pieceType = int((7-i)/2 % 4 + 1)
            
            self.pieces.append(Piece(2, i, 0, pieceType))
            self.pieces.append(Piece(1, i, 6, pieceType))

        # Create the platforms
        for i in range(8):
            for j in range(8):
                # Calculate the height of the platform based on its position

                # top left - quadrant 1
                if i < 4 and j < 4:
                    self.board[i][j] = min(7-i, 7-j)
                
                # bottom right - quadrant 3
                elif i >= 4 and j >= 4:
                    self.board[i][j] = min(i, j)

                # top right - quadrant 2
                elif i < 4 and j >= 4:
                    self.board[i][j] = max(i, 7-j)

                # bottom left - quadrant 4
                else:
                    self.board[i][j] = max(7-i, j)

    def copy(self):
        new_state = GameState()
        new_state.pieces = [piece.copy() for piece in self.pieces]
        new_state.board = [row[:] for row in self.board]
        return new_state
    
    def make_move(self, move):
        """
        Apply a move to the game state.
        move: A tuple containing the piece to move and the new position
        """
        
        piece, (x, y) = move
        # Store the original position of the piece
        original_position = (piece.x, piece.y)
        piece.move(x, y)

        self.moves_history.append((move, original_position))

        if self.model.is_capturing_move(piece, x, y):
            target_piece = self.model.get_piece(x, y)
            self.captured_pieces.append((target_piece, (x, y)))
            self.model.capture_piece(target_piece)

    def undo_move(self):
        """
        Undo a move from the game state.
        """

        (piece, (x, y)), (original_x, original_y) = self.moves_history.pop()
        piece.move(original_x, original_y)

        if self.captured_pieces and self.captured_pieces[-1][1] == (x, y):
            captured_piece, _ = self.captured_pieces.pop()
            self.model.uncapture_piece(captured_piece)

    def get_valid_moves(self, player):
        """
        Get all valid moves for the given player.
        player: The player to get the moves for
        """
        valid_moves = []
        for piece in self.pieces:
            if piece.player == player:
                for i in range(8):
                    for j in range(8):
                        if self.model.check_move(piece, i, j):
                            valid_moves.append((piece, (i, j)))

        # Print the valid moves in a readable format
        """ print("Valid Moves:")
        for move in valid_moves:
            print(move[0], move[1]) """
            
        
        return valid_moves

