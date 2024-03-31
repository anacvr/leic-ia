import random


class GameAI:
    def __init__(self, game_model):
        self.game_model = game_model
        self.pieces = game_model.pieces

    # TODO: function to determine the distance between the T piece and a piece from the opponent 
    #       - check if the T piece is on a lower diagonal cell
    #       - ~~check if the capturing piece is on one of the six cells surronding the T piece~~


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

        # If T piece is not found, return -1
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
    
    def count_opponent_pieces_n_size(self, player, size):
        """
        Counts the number of pieces left on the board, with a specific size, for the opponent of the player.
        """
        count = 0

        for piece in self.pieces:
            if piece.player != player and piece.size == size:
                count += 1

        return count


    def heuristic1(self, player):
        """
        Heuristic 1:
            The score increases if the T player piece gets closer to the goal position.
        """
        
        score = 14 # maximum distance between the T piece and the goal
        
        distance = self.calc_T_distance_to_goal(player)

        if distance == -1:
            print("Error Calculating T distance to goal")
            return 0
        
        score -= distance

        # print("Heuristic 1 Score:", score)

        return score * 10


    def heuristic2(self, player):
        """
        Heuristic 2:
            The score decreases as the number of opponent pieces around the T piece increases.
        """
        
        score = 8 # maximum number of opponent pieces that can be around the T piece

        n_opp_on_radius = self.check_T_radius(player)
        score -= n_opp_on_radius

        # print("Heuristic 2 Score:", score)

        return score * 2

    def heuristic3(self, player):
        """
        Heuristic 3:
            The score of the player increases immensely when it captures the opponent's T piece.
        """

        score = 0

        # Find T piece of the player
        for piece in self.pieces:
            if piece.isTpiece and piece.player != player:
                return score

        # If T piece is not found, score increases
        score = 1

        return score * 1000
    
    def heuristic4(self, player):
        """
        Heuristic 4:
            The score increases as the number of opponent pieces decrease.
            And bigger size pieces value more.
        """

        score = 0

        for size in range(1, 4):
            n_opp_pieces = self.count_opponent_pieces_n_size(player, size)
            score += n_opp_pieces * size
        
        max_score = 40

        return max_score - score
    
    def heuristic5(self, player):
        """
        Heuristic 5:
            The score decreases immensely if the player's T piece can be eaten in the next move.
            TODO: NOT WORKING!!! THIS HEURISTIC NEVER PRINTS THE WARNING IF THE PIECE IS BEING THREATENED WHYYYYYYY
        """
        score = 0

        # Find T piece of the player
        for piece in self.pieces:
            if piece.isTpiece and piece.player == player:
                T_piece = piece
                break

        # Iterate through opponent's pieces to see if there is a threat
        for piece in self.pieces:
            if piece.player != player:
                if self.game_model.is_cell_lower(piece.x, piece.y, T_piece.x, T_piece.y) and \
                self.game_model.is_cell_diagonally_adjacent(piece.x, piece.y, T_piece.x, T_piece.y):
                    score += -10000
        
        if score < 0:
            print("T-piece of player " + player + " is being threatened!")

        return score



    def evaluate(self, player):
        """
        Evaluate the current game state and return a score.
        """
        eval = self.heuristic1(player) + self.heuristic2(player) + self.heuristic3(player) + self.heuristic4(player) + self.heuristic5(player)

        return eval
    

    def minimax(self, game_state, depth, player, alpha, beta, valid_moves=None):
        if depth == 0:
            return self.evaluate(player) + random.uniform(0, 0.01), None

        if valid_moves is None:
            valid_moves = game_state.get_valid_moves(player)

        if player == 1:
            max_eval = float('-inf')
            best_move = None

            for move in valid_moves:
                game_state.make_move(move)
                eval = self.minimax(game_state, depth - 1, 2, alpha, beta, valid_moves)[0]
                game_state.undo_move()

                if eval > max_eval:
                    max_eval = eval
                    best_move = move

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval, best_move

        else:
            min_eval = float('inf')
            best_move = None

            for move in valid_moves:
                game_state.make_move(move)
                eval = self.minimax(game_state, depth - 1, 1, alpha, beta, valid_moves)[0]
                game_state.undo_move()

                if eval < min_eval:
                    min_eval = eval
                    best_move = move

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval, best_move


    def get_best_move(self, game_state, depth, player):
        _, best_move = self.minimax(game_state, depth, player, float('-inf'), float('inf'))
        if best_move is None:
            return None
        return best_move