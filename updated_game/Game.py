class Game:
    def isCollision(self,x1,y1,x2,y2,step_size):
        # top left corner (x1,y1) inside the square formed by x2,y2
        # top right corner (x1 + step_size,y1) inside the square formed by x2,y2
        
        corners = [(x1, y1), (x1 + step_size, y1), (x1, y1 + step_size), (x1 + step_size, y1 + step_size)]
        
        for corner in corners:
            if corner[0] >= x2 and corner[0] <= x2 + step_size:
                if corner[1] >= y2 and corner[1] <= y2 + step_size:
                    return True

       
       
        return False