from pygame.locals import *

class Bricks:
    x = []
    y = []
    step = 44
 
    def __init__(self,x,y, brick_layout_type=0):
        self.initial_x = x * self.step
        self.initial_y = y * self.step
        self.x = [self.initial_x]
        self.y = [self.initial_y]
        self.brick_layout_type = brick_layout_type


 
    def draw(self, surface, image):
        if self.brick_layout_type == 0:
            length = 5
            for i in range(0, length):
                self.x.append(self.initial_x)

                vertical_pos = self.initial_y + (i * self.step) 
                self.y.append(vertical_pos)
                
                surface.blit(image,(self.initial_x, vertical_pos)) 

    def getNumBricks(self):
        return len(self.x)
         