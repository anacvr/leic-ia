class GameAI:
    def __init__(self, game_model):
        self.game_model = game_model
        self.pieces = game_model.pieces
    # TODO: function to determine the distance between the T piece and the cell across the board
    # TODO: function to determine the distance between the T piece and a piece from the opponent 
    #       - check if the T piece is on a lower diagonal cell
    #       - check if the capturing piece is on one of the six cells surronding the T piece

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

