class GameAI:
    def __init__(self, game_model):
        self.game_model = game_model
        self.pieces = game_model.pieces

    # TODO: function to determine the distance between the T piece and a piece from the opponent 
    #       - check if the T piece is on a lower diagonal cell
    #       - check if the capturing piece is on one of the six cells surronding the T piece
        
    def calc_T_distance_to_goal(self, x, y, player):
        """
        Determine the distance between the T piece and the cell across the board.
        (x, y) - coordinates of the T piece
        """
        if player == 1:
            goal = (7, 0)
        else:
            goal = (0, 7)

        return abs(goal[0] - x) + abs(goal[1] - y)
        
    def heuristic1(self, player):
        """
        Heuristic 1:
            The score increases as the T player piece gets closer to the goal position.
        """
        
        print("Evaluating game state for player", player)
        
        score = 14 # 14 is the maximum distance between the T piece and the goal
        T_piece = None

        
        # Find T piece of the player
        for piece in self.pieces:
            if piece.isTpiece and piece.player == player:
                T_piece = piece
                break

        # If T piece is not found, return 0
        if T_piece is None:
            return 0
        
        score -= self.calc_T_distance_to_goal(T_piece.x, T_piece.y, player)

        print("Heuristic 1 Score:", score)

        return score

    def evaluate(self, player):
        """
        Evaluate the current game state and return a score.
        """
        
        eval = self.heuristic1(player)

        return eval

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

