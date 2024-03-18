import heuristics

class GameAI:
    def __init__(self, game_model):
        self.game_model = game_model

    # TODO: function to determine the distance between the T piece and a piece from the opponent 
    #       - check if the T piece is on a lower diagonal cell
    #       - ~~check if the capturing piece is on one of the six cells surronding the T piece~~



    def evaluate(self, player):
        """
        Evaluate the current game state and return a score.
        """
        print("Evaluating game state for player", player)
        
        eval = heuristics.heuristic1(player)
        eval += heuristics.heuristic2(player)

        return eval
    
    
    def minimax(self, game_state, depth, player):
        """
        Perform a minimax search.
        depth: The depth of the search tree
        player: The current player (1 or 2)
        """
        
        if depth == 0:
            return self.evaluate(player)
        
        if player == 2:
            best_value = float('inf')
            for move in game_state.get_valid_moves():
                game_state.make_move(move)
                value = self.minimax(depth - 1, 2)
                game_state.undo_move(move)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = float('-inf')
            for move in game_state.get_valid_moves():
                game_state.make_move(move)
                value = self.minimax(depth - 1, 1)
                game_state.undo_move(move)
                best_value = min(best_value, value)
            return best_value
        

    def get_next_move_minimax(self, game_state):
        """
        Determine the AI's next move utilizing the minimax algorithm.
        """
        
        best_move = None
        best_value = float('-inf')
        
        # MINIMAX SEARCH
        # Iterate through all valid moves
        for move in game_state.get_valid_moves():
            # Make the move and evaluate the game state
            game_state.make_move(move)
            value = self.minimax(game_state, 3, 2)

            # Undo the move
            game_state.undo_move(move)

            if value > best_value:
                best_value = value
                best_move = move
        
        return best_move

