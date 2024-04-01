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
    
    def heuristic_player_win(self, player):
        """
        The score is + infinity if the player wins the game.
        """

        if self.game_model.is_game_over():
            if player == 1:
                return float('inf')
            else:
                return float('-inf')
        
        return 0



    def heuristic1(self, player):
        """
        Heuristic 1:
            The score increases if the T player piece gets closer to the goal position.
        """
        
        score = 14 # maximum distance between the T piece and the goal
        
        distance = self.calc_T_distance_to_goal(player)
        
        score -= distance

        return score * 10


    def heuristic2(self, player):
        """
        Heuristic 2:
            The score decreases as the number of opponent pieces around the T piece increases.
        """
        
        score = 8 # maximum number of opponent pieces that can be around the T piece

        n_opp_on_radius = self.check_T_radius(player)
        score -= n_opp_on_radius

        return score * 2

    def heuristic3(self, player):
        """
        Heuristic 3:
            The score of the player increases immensely when it captures the opponent's T piece.
        """

        score = 1000

        # Find T piece of the player
        for piece in self.pieces:
            if piece.isTpiece and piece.player != player:
                return -10000

        return score
    
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
                    score = -10000
                    break
        
        return score

    def heuristic6(self, player):
        """
        Heuristic 6:
            The score increases immensely if the AI can eat the opponent's T piece in the next move.
        """
        score = 10000  # High score to prioritize eating the opponent's T piece

        # Find the opponent's T piece
        opponent_T_piece = None
        for piece in self.pieces:
            if piece.isTpiece and piece.player != player:
                opponent_T_piece = piece
                break

        # If the opponent's T piece is not found, return 0
        if opponent_T_piece is None:
            return 0

        # Iterate over all pieces of the AI
        for piece in self.pieces:
            if piece.player == player:
                # Check if the AI's piece can eat the opponent's T piece in the next move
                if self.game_model.is_cell_lower(piece.x, piece.y, opponent_T_piece.x, opponent_T_piece.y) and \
                self.game_model.is_cell_diagonally_adjacent(piece.x, piece.y, opponent_T_piece.x, opponent_T_piece.y):
                    return score  # Return the high score if the AI can eat the opponent's T piece

        return 0  # Return 0 if the AI cannot eat the opponent's T piece in the next move

    def evaluate(self, player):
        """
        Evaluate the current game state and return a score.
        """
        eval = self.heuristic1(player) + self.heuristic2(player) + self.heuristic4(player) + self.heuristic5(player) + self.heuristic6(player)

        #print("Evaluation of the move: " + str(eval))
        return eval
    

    def minimax(self, game_state, depth, max_player, player, alpha, beta, valid_moves=None):
        if depth == 0:
            return self.evaluate(max_player) + random.uniform(0, 0.01), None

        if valid_moves is None:
            valid_moves = game_state.get_valid_moves(player)

        if player == max_player:
            max_eval = float('-inf')
            best_move = None

            for move in valid_moves:
                game_state.make_move(move)
                eval = self.minimax(game_state, depth - 1, max_player, 1, alpha, beta, valid_moves)[0]
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
                eval = self.minimax(game_state, depth - 1, max_player, 2, alpha, beta, valid_moves)[0]
                game_state.undo_move()

                if eval < min_eval:
                    min_eval = eval
                    best_move = move

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval, best_move


    def get_best_move(self, game_state, depth, player):
        _, best_move = self.minimax(game_state, depth, player, player, float('-inf'), float('inf'))
        if best_move is None:
            return None
        return best_move