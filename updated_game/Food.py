from pygame.locals import *
from random import randint

class Food:
    x = 0
    y = 0
    step = 44

    def __init__(self):
        pass

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))

    def generate_food(self, snake, bricks):
        self.x = randint(1,16) * self.step
        self.y = randint(1,12) * self.step
    # windowWidth = 800
    # windowHeight = 600
        print("X={0} Y={1}".format(self.x, self.y))

        # generate a new food point if it overlaps with one of the brick's position
        for i in range(bricks.getNumBricks()):
            if bricks.x[i] == self.x and bricks.y[i] == self.y:
                print("Generated at position of brick")
                return self.generate_food(snake, bricks)
