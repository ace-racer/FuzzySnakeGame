from Game import Game
import constants
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import math as m


#To Calculate the angle between 2 points

#myradians = math.atan2(targetY-gunY, targetX-gunX)

class FuzzyRulesController:


    def __init__(self, max_moves=1000):
        self.max_moves = max_moves
        self.current_move_number = 0
        self.game = Game()
        self.mf_pm_right()
        self.mf_pm_left()
        self.mf_pm_up()
        self.mf_pm_down()


    def mf_pm_right(self):
        '''if the previous move is RIGHT, the only direciton
        you can move is UP, RIGHT, DOWN'''
        self.next_move_pm_right = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_right['up'] = fuzz.trimf(self.next_move_pm_right.universe,[0,25, 50])
        self.next_move_pm_right['right'] = fuzz.trimf(self.next_move_pm_right.universe,[25,50,75])
        self.next_move_pm_right['down'] = fuzz.trimf(self.next_move_pm_right.universe,[50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['right'] = fuzz.trimf(self.food_loc.universe,[45,135,180])
        self.food_loc['left'] = fuzz.trimf(self.food_loc.universe, [-180,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_right['right'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_right['up'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_right['down'])

    def mf_pm_left(self):
        '''if the previous move is LEFT, the only direciton
        you can move is UP, LEFT, DOWN'''
        self.next_move_pm_left = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_left['up'] = fuzz.trimf(self.next_move_pm_left.universe,[0,25, 50])
        self.next_move_pm_left['left'] = fuzz.trimf(self.next_move_pm_left.universe,[25,50,75])
        self.next_move_pm_left['down'] = fuzz.trimf(self.next_move_pm_left.universe,[50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['left'] = fuzz.trimf(self.food_loc.universe,[45,135,180])
        self.food_loc['right'] = fuzz.trimf(self.food_loc.universe, [-180,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_left['left'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_left['down'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_left['up'])


    def mf_pm_up(self):
        '''if the previous move is UP, the only direciton
        you can move is UP, LEFT, RIGHT'''
        self.next_move_pm_up = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_up['left'] = fuzz.trimf(self.next_move_pm_up.universe,[0,25, 50])
        self.next_move_pm_up['up'] = fuzz.trimf(self.next_move_pm_up.universe,[25,50,75])
        self.next_move_pm_up['right'] = fuzz.trimf(self.next_move_pm_up.universe, [50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['left'] = fuzz.trimf(self.food_loc.universe,[45,135,180])
        self.food_loc['right'] = fuzz.trimf(self.food_loc.universe, [-180,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_up['up'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_up['left'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_up['right'])
    #
    def mf_pm_down(self):
        '''if the previous move is DOWN, the only direciton
        you can move is DOWN, LEFT, RIGHT'''
        self.next_move_pm_down = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_down['left'] = fuzz.trimf(self.next_move_pm_down.universe,[0,25, 50])
        self.next_move_pm_down['down'] = fuzz.trimf(self.next_move_pm_down.universe,[25,50,75])
        self.next_move_pm_down['right'] = fuzz.trimf(self.next_move_pm_down.universe,[50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['left'] = fuzz.trimf(self.food_loc.universe,[45,135,180])
        self.food_loc['right'] = fuzz.trimf(self.food_loc.universe, [-180,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_down['down'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_down['right'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_down['left'])


    def get_angle_pm_right(self,food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
        print(str(food_y) + " " + str(food_x) + " " + str(snake_y) +" " + str(snake_x))
        angle = m.degrees(m.atan2((food_y-snake_y),(food_x - snake_x)))
        if angle <= 90 and angle >= 0:
            final_angle = angle
        if angle >= 90 and angle <= 180:
            final_angle = angle
        if  -90 <=angle <= 0:
            final_angle = angle
        if angle >= -180 and angle <= -90:
            final_angle = angle
        return int(final_angle)

    def get_angle_pm_left(self,food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
        print(str(food_y) + " " + str(food_x) + " " + str(snake_y) +" " + str(snake_x))
        angle = m.degrees(m.atan2((food_y-snake_y),(food_x - snake_x)))
        if angle <= 90 and angle >= 0:
            final_angle = 180-angle
        if angle >= 90 and angle <= 180:
            final_angle = 180-angle
        if  -90 <=angle <= 0:
            final_angle = -180 - angle
        if angle >= -180 and angle <= -90:
            final_angle = -180 - angle
        return int(final_angle)

    def get_angle_pm_up(self,food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
        print(str(food_y) + " " + str(food_x) + " " + str(snake_y) +" " + str(snake_x))
        angle = m.degrees(m.atan2((food_y-snake_y),(food_x - snake_x)))
        if angle <= 90 and angle >= 0:
            final_angle = 90 - angle
        if angle >= 90 and angle <= 180:
            final_angle = -(angle-90)
        if  -90 <=angle <= 0:
            final_angle = 90 -angle
        if angle >= -180 and angle <= -90:
            final_angle = (180 + angle) + 90
        return int(final_angle)

    def get_angle_pm_down(self,food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
        print(str(food_y) + " " + str(food_x) + " " + str(snake_y) +" " + str(snake_x))
        angle = m.degrees(m.atan2((food_y-snake_y),(food_x - snake_x)))
        if angle <= 90 and angle >= 0:
            final_angle = -90 - angle
        if angle >= 90 and angle <= 180:
            final_angle = 180 - angle + 90
        if  -90 <=angle <= 0:
            final_angle = -(90-angle)
        if angle >= -180 and angle <= -90:
            final_angle = -angle -90
        return int(final_angle)


    def perform_next_move(self, snake, food, bricks):
        if self.current_move_number < self.max_moves:
            if snake.direction == constants.RIGHT:
                self.mf_pm_right()
                angle = self.get_angle_pm_right(food.y, food.x, snake.y[0], snake.x[0])
                print(angle)
                next_move_crtl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                result = int(next_move_crtl_fuzzy.output['Next Direction'])
                print(str(result)+"lulz" )
                if result < 33:
                    snake.moveUp()
                    print("Move up1")
                if result >=33 and result <=67:
                    snake.moveRight()
                    print("Move right2")
                if result >=68:
                    snake.moveDown()
                    print("Move down3")

            elif snake.direction == constants.LEFT:
                self.mf_pm_left()
                angle = self.get_angle_pm_left(food.y, food.x, snake.y[0], snake.x[0])
                print(angle)
                next_move_crtl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                result = int(next_move_crtl_fuzzy.output['Next Direction'])

                print(str(result)+"lulz" )
                if result < 33:
                    snake.moveUp()
                    print("Move up4")
                if result >=33 and result <=67:
                    snake.moveLeft()
                    print("Move Left5")
                else:
                    snake.moveDown()
                    print("Move Down6")

            elif snake.direction == constants.UP:
                self.mf_pm_up()
                angle = self.get_angle_pm_up(food.y, food.x, snake.y[0], snake.x[0])
                print(angle)
                next_move_crtl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                result = int(next_move_crtl_fuzzy.output['Next Direction'])
                print(str(result)+"lulz" )
                if result < 33:
                    snake.moveLeft()
                    print("Move Left7")
                if result >=33 and result <=67:
                    snake.moveUp()
                    print("Move up8")
                else:
                    snake.moveRight()
                    print("Move Right9")

            elif snake.direction == constants.DOWN:
                self.mf_pm_down()
                angle = self.get_angle_pm_down(food.y, food.x, snake.y[0], snake.x[0])
                print(angle)
                next_move_crtl = ctrl.ControlSystem([self.rule1, self.rule2, self.rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                result = int(next_move_crtl_fuzzy.output['Next Direction'])
                print(str(result)+"lulz" )
                if result < 33:
                    snake.moveRight()
                    print("Move Left10")
                if result >=33 and result <=67:
                    snake.moveDown()
                    print("Move up11")
                else:
                    snake.moveLeft()
                    print("Move Right12")


            self.current_move_number += 1
            return snake, True
        return snake, False

