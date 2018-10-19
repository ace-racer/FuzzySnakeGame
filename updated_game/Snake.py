from pygame.locals import *
import constants

class Snake:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3

    updateCountMax = 2
    updateCount = 0

    def __init__(self, length, window_height=600, window_width=800):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)

       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44

       self._window_height = window_height
       self._window_width = window_width

    def update(self):

        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:

            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            # update position of head of snake
            if self.direction == constants.RIGHT:
                if self.x[0] + self.step >= self._window_width:
                    self.x[0] = 0
                else:
                    self.x[0] = self.x[0] + self.step
            if self.direction == constants.LEFT:
                if self.x[0] - self.step <= 0:
                    self.x[0] = self._window_width - self.step
                else:
                    self.x[0] = self.x[0] - self.step
            if self.direction == constants.UP:
                if self.y[0] - self.step <= 0:
                    self.y[0] = self._window_height - self.step
                else:
                    self.y[0] = self.y[0] - self.step

            if self.direction == constants.DOWN:
                if self.y[0] + self.step >= self._window_height:
                    self.y[0] = 0
                else:
                    self.y[0] = self.y[0] + self.step

            self.updateCount = 0


    def moveRight(self):
        self.direction = constants.RIGHT

    def moveLeft(self):
        self.direction = constants.LEFT

    def moveUp(self):
        self.direction = constants.UP

    def moveDown(self):
        self.direction = constants.DOWN

    def getCurrentDirection(self):
        return self.direction

    def draw(self, surface, image, head_image):
        surface.blit(head_image,(self.x[0],self.y[0]))
        for i in range(1,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

    def get_distance_from_wall(self, bricks, direction):
        """
            Get the distance of the snake from the brick wall given that the snake moves in the provided direction
        """
        num_bricks = bricks.getNumBricks()
        closest_distance = constants.MAX_VAL

        for itr in range(num_bricks):
            current_distance = constants.MAX_VAL
            if direction == constants.UP or direction == constants.DOWN:
                # if the brick is directly above or below the snake
                if bricks.x[itr] == self.x[0]:
                    current_distance = abs(bricks.y[itr] - self.y[0])

            if direction == constants.LEFT or direction == constants.RIGHT:
                # if the brick is directly to the left or right of the snake
                if bricks.y[itr] == self.y[0]:
                    current_distance = abs(self.x[0] - bricks.x[itr])

            if current_distance < closest_distance:
                closest_distance = current_distance

        return closest_distance

    def will_snake_collide_with_itself_for_direction(self, direction):
        """Will the snake collide with itself if it proceeds in the direction provided"""
        snake_head_x = self.x[0]
        snake_head_y = self.y[0]
        for itr in range(1, self.length):
            if self.y[itr] == snake_head_y:
                if direction == constants.RIGHT:
                    if abs(snake_head_x + self.step - self.x[itr]) <= 1.5 * constants.STEP_SIZE:
                        return True

                if direction == constants.LEFT:
                    if abs(snake_head_x - self.step - self.x[itr]) <= 1.5 * constants.STEP_SIZE:
                        return True

            elif self.x[itr] == snake_head_x:
                if direction == constants.UP:
                    if abs(snake_head_y - self.step - self.y[itr]) <= 1.5 * constants.STEP_SIZE:
                        return True

                if direction == constants.DOWN:
                    if abs(snake_head_y + self.step - self.y[itr]) <= 1.5 * constants.STEP_SIZE:
                        return True



        return False
