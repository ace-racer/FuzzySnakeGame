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
            
            # if the food is to the left of the snake
            if food.x < snake.x[0] and not snake.will_snake_collide_with_itself_for_direction(constants.LEFT):
                distance_from_wall = snake.get_distance_from_wall(bricks, constants.LEFT)
                if not self.is_distance_too_less(distance_from_wall):
                    snake.moveLeft()
                else:
                    snake.moveDown()
            # if food is to the right of the snake
            elif food.x > snake.x[0] and not snake.will_snake_collide_with_itself_for_direction(constants.RIGHT):
                distance_from_wall = snake.get_distance_from_wall(bricks, constants.RIGHT)
                if not self.is_distance_too_less(distance_from_wall):
                    snake.moveRight()
                else:
                    snake.moveUp()
            else:
                # the head of snake is at same column as the food
            
                # snake is lower than the food
                if food.y < snake.y[0] and not snake.will_snake_collide_with_itself_for_direction(constants.UP):
                    distance_from_wall = snake.get_distance_from_wall(bricks, constants.UP)
                    if not self.is_distance_too_less(distance_from_wall):
                        snake.moveUp()
                    else:
                        snake.moveLeft()
                # snake is higher than the food
                elif food.y > snake.y[0] and not snake.will_snake_collide_with_itself_for_direction(constants.DOWN):
                    distance_from_wall = snake.get_distance_from_wall(bricks, constants.DOWN)
                    if not self.is_distance_too_less(distance_from_wall):
                        snake.moveDown()
                    else:
                        snake.moveRight()
            
            self.current_move_number += 1
            return snake, True
        return snake, False

    def is_distance_too_less(self, distance):
        if distance <= (2 * constants.STEP_SIZE):
            return True
        return False

            


            