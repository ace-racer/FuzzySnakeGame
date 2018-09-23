from Game import Game
import constants

class RuleBasedController:
    def __init__(self, max_moves=1000):
        self.max_moves = max_moves
        self.current_move_number = 0
        self.game = Game()

    def perform_next_move(self, snake, food, bricks):
        if self.current_move_number < self.max_moves:
            current_snake_direction = snake.getCurrentDirection()

            # if the food is to the left of the snake
            if food.x < snake.x[0]:
                snake.moveLeft()
            # if food is to the right of the snake
            elif food.x > snake.x[0] and current_snake_direction != constants.LEFT:
                snake.moveRight()
            else:
                # the head of snake is at same column as the food
            
                # snake is lower than the food
                if food.y < snake.y[0] and current_snake_direction != constants.DOWN:
                    snake.moveUp()
                # snake is higher than the food
                elif food.y > snake.y[0]:
                    snake.moveDown()
            
            self.current_move_number += 1
            return snake, True
        return snake, False

            


            