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
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 