class GameAI:
    def __init__(self, game_model):
        self.game_model = game_model
        self.pieces = game_model.pieces

    # TODO: function to determine the distance between the T piece and a piece from the opponent 
    #       - check if the T piece is on a lower diagonal cell
    #       - check if the capturing piece is on one of the six cells surronding the T piece


    def calc_T_distance_to_goal(self, player):
        """
        Determine the distance between the T piece and the cell across the board.
        (x, y) - coordinates of the T piece
        """
        T_piece = None

        # Find T piece of the player
        for piece in self.pieces:
            if piece.isTpiece and piece.player == player:
                T_piece = piece
                break

        # If T piece is not found, return 0
        if T_piece is None:
            return -1
        
        if player == 1:
            goal = (7, 0)
        else:
            goal = (0, 7)


        return abs(goal[0] - T_piece.x) + abs(goal[1] - T_piece.y)


    def check_T_radius(self, player):
        """
        Check if the T piece has an opponent piece within its radius (8 cells around it).
        """

        T_piece = None

        # Find T piece of the player
        for piece in self.pieces:
            if piece.isTpiece and piece.player == player:
                T_piece = piece
                break

        # If T piece is not found, return 0
        if T_piece is None:
            return -1

        count = 0

        # Check if there is an opponent piece within the T piece radius
        for piece in self.pieces:
            if piece.player != player:
                if abs(T_piece.x - piece.x) <= 1 and abs(T_piece.y - piece.y) <= 1:
                    count += 1

        return count


    def heuristic1(self, player):
        """
        Heuristic 1:
            The score increases as the T player piece gets closer to the goal position.
        """
        
        score = 14 # maximum distance between the T piece and the goal
        
        distance = self.calc_T_distance_to_goal(player)

        if distance == -1:
            print("Error Calculating T distance to goal")
            return 0
        
        score -= distance

        # print("Heuristic 1 Score:", score)

        return score
    

    def heuristic2(self, player):
        """
        Heuristic 2:
            The score decreases as the number of opponent pieces around the T piece increases.
        """
        
        score = 8 # maximum number of opponent pieces that can be around the T piece

        n_opp_on_radius = self.check_T_radius(player)
        score -= n_opp_on_radius

        # print("Heuristic 2 Score:", score)

        return score

    def evaluate(self, player):
        """
        Evaluate the current game state and return a score.
        """
        print("Evaluating game state for player", player)
        
        eval = self.heuristic1(player)
        eval += self.heuristic2(player)

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

