import random


class GameAI:
    def __init__(self, game_model, depth):
        self.game_model = game_model
        self.pieces = game_model.pieces
        self.depth = depth
        self.turn_count_1 = 0
        self.turn_count_2 = 0

    # TODO: function to determine the distance between the T piece and a piece from the opponent 
    #       - check if the T piece is on a lower diagonal cell
    #       - ~~check if the capturing piece is on one of the six cells surronding the T piece~~


    def calc_T_distance_to_goal(self, game_state, player):
        """
        Determine the distance between the T piece and the cell across the board.
        (x, y) - coordinates of the T piece
        """
        T_piece = None

        # Find T piece of the player
        for piece in game_state.pieces:
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


    def check_T_radius(self, game_state, player):
        """
        Check if the T piece has an opponent piece within its radius (8 cells around it).
        """

        T_piece = None

        # Find T piece of the player
        for piece in game_state.pieces:
            if piece.isTpiece and piece.player == player:
                T_piece = piece
                break

        # If T piece is not found, return 0
        if T_piece is None:
            return -1

        count = 0

        # Check if there is an opponent piece within the T piece radius
        for piece in game_state.pieces:
            if piece.player != player:
                if abs(T_piece.x - piece.x) <= 1 and abs(T_piece.y - piece.y) <= 1:
                    count += 1

        return count
    
    def count_opponent_pieces_n_size(self, game_state, player, size):
        """
        Counts the number of pieces left on the board, with a specific size, for the opponent of the player.
        """
        count = 0

        for piece in game_state.pieces:
            if piece.player != player and piece.size == size:
                count += 1

        return count


    def heuristic1(self, game_state, player):
        """
        Heuristic 1:
            The score increases if the T player piece gets closer to the goal position.
        """
        
        score = 14 - self.calc_T_distance_to_goal(game_state, player)
        return score * 10


    def heuristic2(self, game_state, player):
        """
        Heuristic 2:
            The score decreases as the number of opponent pieces around the T piece increases.
        """
        
        score = 8 - self.check_T_radius(game_state, player)
        return score * 2

    def heuristic3(self, game_state, player, valid_moves):
        """
        Heuristic 3:
            The score of the player increases immensely when it captures the opponent's T piece.
        """

        score = 0

        # Find T piece of the player
        for piece in game_state.pieces:
            if piece.isTpiece and piece.player != player:
                goal_x = piece.x
                goal_y = piece.y

        for move in valid_moves:
            piece, (x,y) = move
            if (x, y) == (goal_x, goal_y):
                score = 100000
                

        return score
    
    def heuristic4(self, game_state, player):
        """
        Heuristic 4:
            The score increases as the number of opponent pieces decrease.
            And bigger size pieces value more.
        """

        score = 0

        for size in range(1, 4):
            n_opp_pieces = self.count_opponent_pieces_n_size(game_state, player, size)
            score += n_opp_pieces * size
        
        max_score = 40

        return max_score - score
    
    def heuristic5(self, game_state, player):
        """
        Heuristic 5:
            The score decreases immensely if the player's T piece can be eaten in the next move.
        """
        score = 0

        # Find T piece of the player
        for piece in game_state.pieces:
            if piece.isTpiece and piece.player == player:
                T_piece = piece
                break

        # Iterate through opponent's pieces to see if there is a threat
        for piece in game_state.pieces:
            if piece.player != player:
                if self.game_model.is_cell_lower(piece.x, piece.y, T_piece.x, T_piece.y) and \
                self.game_model.is_cell_diagonally_adjacent(piece.x, piece.y, T_piece.x, T_piece.y):
                    score = -10000
                    break
        
        return score

    def heuristic6(self, game_state, player):
        """
        Heuristic 6:
            The score increases immensely if the AI can eat the opponent's T piece in the next move.
        """
        score = 10000

        # Find the opponent's T piece
        opponent_T_piece = None
        for piece in game_state.pieces:
            if piece.isTpiece and piece.player != player:
                opponent_T_piece = piece
                break

        # If the opponent's T piece is not found, return 0
        if opponent_T_piece is None:
            return 0

        # Iterate over all pieces of the AI
        for piece in game_state.pieces:
            if piece.player == player:
                # Check if the AI's piece can eat the opponent's T piece in the next move
                if self.game_model.is_cell_lower(piece.x, piece.y, opponent_T_piece.x, opponent_T_piece.y) and \
                self.game_model.is_cell_diagonally_adjacent(piece.x, piece.y, opponent_T_piece.x, opponent_T_piece.y):
                    return score

        # Return 0 if the AI cannot eat the opponent's T piece in the next move
        return 0

    def evaluate(self, game_state, player, valid_moves):
        """
        Evaluate the current game state and return a score.
        """
        if self.depth == 2:
            score = self.heuristic1(game_state, player) + self.heuristic2(game_state, player)
            
        if self.depth == 3:
            score = (
                self.heuristic1(game_state, player) +  # Distance to goal
                self.heuristic2(game_state, player) +  # Number of opponent pieces around T piece
                self.heuristic3(game_state, player, valid_moves) +  # Capture opponent's T piece
                self.heuristic4(game_state, player)    # Number and size of opponent pieces
            )
            
        if self.depth == 4:
            score = (
                self.heuristic1(game_state, player) +  # Distance to goal
                self.heuristic3(game_state, player, valid_moves) +  # Capture opponent's T piece
                self.heuristic4(game_state, player) +  # Number and size of opponent pieces
                self.heuristic5(game_state, player) +  # Threat to player's T piece
                self.heuristic6(game_state, player)    # Opportunity to capture opponent's T piece
            )

        return score
    
    def eval_terminal_state(self, player, winner):
        if player == winner:
            return float('inf')
        else:
            return float('-inf')

    def minimax(self, game_state, depth, max_player, player, alpha, beta, valid_moves=None):
        if depth == 0:

            return self.evaluate(game_state, max_player, valid_moves) + random.uniform(0, 0.01), None
        
        # Check if this is a terminal state
        winner = self.game_model.is_game_over(game_state)
        if winner is not None:
            return self.eval_terminal_state(max_player, winner), None
            

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

            peça, (x,y) = best_move                
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
        return best_move