from Game import Game
import constants

class RuleBasedController:
    def __init__(self, max_moves=1000):
        self.max_moves = max_moves
        self.current_move_number = 0
        self.game = Game()
        self._MAX = 9999999999

    def perform_next_move(self, snake, food, bricks):
        if self.current_move_number < self.max_moves:
            current_snake_direction = snake.getCurrentDirection()

            # if the food is to the left of the snake
            if food.x < snake.x[0] and current_snake_direction != constants.RIGHT:
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
                elif food.y > snake.y[0] and current_snake_direction != constants.UP:
                    snake.moveDown()
            
            self.current_move_number += 1
            return snake, True
        return snake, False

    def get_distance_from_wall(self, snake, bricks):
        closest_distance_to_brick_x = self._MAX
        closest_distance_to_brick_y = self._MAX
        for itr in range(bricks.getNumBricks()):
            dist_from_snake_head_x = (snake.x[0] - bricks.x[itr])
            dist_from_snake_head_y = (snake.y[0] - bricks.y[itr])

            if abs(dist_from_snake_head_x) < closest_distance_to_brick_x:
                closest_distance_to_brick_x = dist_from_snake_head_x
            
            if abs(dist_from_snake_head_y) < closest_distance_to_brick_y:
                closest_distance_to_brick_y = dist_from_snake_head_y

        return closest_distance_to_brick_x, closest_distance_to_brick_y

            


            