class GameAI:
    def __init__(self, game_model):
        self.game_model = game_model
        self.pieces = game_model.pieces

    def evaluate(self):
        """
        Evaluate the current game state and return a score.
        This function should analyze the gameboard and assign a score to the current state.
        The score can be used to determine the AI's next move.
        """
        # TODO: Implement the evaluation logic here
        # You might want to consider factors like the number of pieces each player has,
        # the positions of the pieces, and the height of the platforms.
        
        pass

    def get_next_move(self):
        """
        Determine the AI's next move based on the current game state.
        This function should use the evaluate() function to evaluate the game state
        and return the AI's next move.
        """
        # TODO: Implement the logic to determine the next move here
        # You might want to consider all possible moves and choose the one that results
        # in the highest score according to the evaluate() function.

        return (self.pieces[1], 1, 1)


    # THIS SHOULD BE IN GAME_MODEL.PY
    def is_game_over(self):
        """
        Check if the game is over.
        This function should return True if the game is over, False otherwise.
        """
        # TODO: Implement the logic to check if the game is over here
        # You might want to check if one player has no pieces left, or if there are no
        # valid moves left.

        for piece in self.pieces:
            # Case 1: The game is over if a T piece is eaten
            if piece.isTpiece and piece.player == 1:
                return False
            elif piece.isTpiece and piece.player == 2:
                return False
            
            # Case 2: The game is over if a T piece reaches the opposite end
            elif piece.isTpiece and piece.player == 1:
                if piece.x == 7 and piece.y == 0:
                    return True
            elif piece.isTpiece and piece.player == 2:
                if piece.x == 0 and piece.y == 7:
                    return True

