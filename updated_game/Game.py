class Game:
    def isCollision(self,x1,y1,x2,y2,item2_size):
        if x1 >= x2 and x1 <= x2 + item2_size:
            if y1 >= y2 and y1 <= y2 + item2_size:
                return True
        return False