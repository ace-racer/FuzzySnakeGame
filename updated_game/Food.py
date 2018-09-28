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
        self.x = randint(2,9) * self.step
        self.y = randint(2,9) * self.step
        
        # generate a new food point if it overlaps with one of the brick's position
        for i in range(bricks.getNumBricks()):
            if bricks.x[i] == self.x and bricks.y[i] == self.y:
                print("Generated at position of brick")
                return self.generate_food(snake, bricks)
