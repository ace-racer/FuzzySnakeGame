from pygame.locals import *

class Bricks:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y, bricks_per_patch=[1]):
        self.x = x * self.step
        self.y = y * self.step
        self._num_patches = len(bricks_per_patch)
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 