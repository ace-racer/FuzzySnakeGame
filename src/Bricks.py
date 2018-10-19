from pygame.locals import *

class Bricks:
    x = []
    y = []
    step = 44
    bricks_length = 5

    def __init__(self,x,y, brick_layout_type=0):
        self.initial_x = x * self.step
        self.initial_y = y * self.step
        self.brick_layout_type = brick_layout_type
        if brick_layout_type != 0:
            self.x = []
            self.y = []


    def draw(self, surface, image):

        # reinitialize the x and y lists representing the bricks for every drawing
        if self.brick_layout_type != 0:
            self.x = []
            self.y = []

        if self.brick_layout_type == 1:
            for i in range(0, self.bricks_length):
                self.x.append(self.initial_x)
                vertical_pos = self.initial_y + (i * self.step)
                self.y.append(vertical_pos)
                surface.blit(image,(self.initial_x, vertical_pos))
        elif self.brick_layout_type == 2:
            for i in range(0, self.bricks_length):
                self.y.append(self.initial_y)
                horizontal_pos = self.initial_x + (i * self.step)
                self.x.append(horizontal_pos)
                surface.blit(image,(horizontal_pos, self.initial_y))
        elif self.brick_layout_type == 3:
            horizontal_pos = self.initial_x

            # first lay the horizontal bricks
            for i in range(0, self.bricks_length):
                self.y.append(self.initial_y)
                horizontal_pos = self.initial_x + (i * self.step)
                self.x.append(horizontal_pos)
                surface.blit(image,(horizontal_pos, self.initial_y))

            # lay the vertical blocks where the horizontal bricks end
            vertical_bricks_x = horizontal_pos
            for i in range(1, self.bricks_length):
                self.x.append(vertical_bricks_x)
                vertical_pos = self.initial_y + (i * self.step)
                self.y.append(vertical_pos)
                surface.blit(image,(vertical_bricks_x, vertical_pos))


    def getNumBricks(self):
        return len(self.x)
