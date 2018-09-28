from pygame.locals import *

class Bricks:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y, brick_layout_type=0):
        self.x = x * self.step
        self.y = y * self.step
        
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 