class Game:
    def isCollision(self,x1,y1,x2,y2,step_size):

        if x1 == x2 and y1 == y2:
            return True

        return False
