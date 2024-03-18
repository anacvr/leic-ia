from piece import Piece

class GameState:
    def __init__(self, game_model):
        self.model = game_model
        self.pieces = []
        self.board = [[0 for _ in range(8)] for _ in range(8)]

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
        print("Making move", move)
        if(len(move) == 2):
            piece, (x, y) = move
        else:
            return
        target_piece = self.model.get_piece(x, y)
        
        # CAPTURE
        # The target cell is diagonally adjacent and on a lower platform level
        # And the target cell contains an opponent's piece with a smaller or equal size
        if self.model.is_cell_lower(piece.x, piece.y, x, y) and \
        self.model.is_cell_diagonally_adjacent(piece.x, piece.y, x, y) and \
        target_piece is not None and \
        target_piece.player != piece.player and \
        piece.size >= target_piece.size:
            self.model.capture_piece(target_piece)
        
        piece.x, piece.y = x, y

    def undo_move(self, move):
        """
        Undo a move from the game state.
        move: A tuple containing the piece to move and the new position
        """
        piece, old_position = move
        piece.x, piece.y = old_position

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
        return valid_moves

