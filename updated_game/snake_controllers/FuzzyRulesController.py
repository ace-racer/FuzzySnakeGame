from Game import Game
import constants

class FuzzyRulesController:
    def __init__(self, max_moves=1000):
        self.max_moves = max_moves
        self.current_move_number = 0
        self.game = Game()

    def perform_next_move(self, snake, food, bricks):
        if self.current_move_number < self.max_moves:
            
            # Fuzzy rules to be put here!

            self.current_move_number += 1
            return snake, True
        return snake, False