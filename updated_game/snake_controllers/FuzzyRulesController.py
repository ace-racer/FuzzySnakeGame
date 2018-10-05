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
        # New Antecedent/Consequent objects hold universe variables and membership functions
        # pm_right = ctrl.Antecedent(np.arange(0, 101, 1), 'pm_right')
        # pm_left = ctrl.Antecedent(np.arange(0, 101, 1), 'pm_left')
        # pm_up = ctrl.Antecedent(np.arange(0, 101, 1), 'pm_up')
        # pm_down = ctrl.Antecedent(np.arange(0, 101, 1), 'pm_down')
        '''if the previous move is RIGHT, the only direciton
        you can move is UP, RIGHT, DOWN'''
        next_move_pm_right = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_right['up'] = fuzz.trimf(next_move_pm_right.universe,[0,25, 50])
        next_move_pm_right['right'] = fuzz.trimf(next_move_pm_right.universe,[25,50,75])
        next_move_pm_right['down'] = fuzz.trimf(next_move_pm_right.universe,[50,75,100])
        food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Angle is based on the 4 quadrant'''

        food_loc['up'] = fuzz.trimf(food_loc.universe,[-90,0, 90])
        food_loc['left'] = fuzz.trimf(food_loc.universe,[45,135,180])
        food_loc['right'] = fuzz.trimf(food_loc.universe, [-180,-135,-45])

    def mf_pm_left(self):
        '''if the previous move is LEFT, the only direciton
        you can move is UP, LEFT, DOWN'''
        next_move_pm_left = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_left['up'] = fuzz.trimf(next_move_pm_left.universe,[0,25, 50])
        next_move_pm_left['left'] = fuzz.trimf(next_move_pm_left.universe,[25,50,75])
        next_move_pm_left['down'] = fuzz.trimf(next_move_pm_left.universe,[50,75,100])

        food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Based on a clock'''

        food_loc['up'] = fuzz.trimf(food_loc.universe,[-90,0, 90])
        food_loc['left'] = fuzz.trimf(food_loc.universe,[45,135,180])
        food_loc['right'] = fuzz.trimf(food_loc.universe, [-180,-135,-45])

    def mf_pm_up(self):
        '''if the previous move is UP, the only direciton
        you can move is UP, LEFT, RIGHT'''
        next_move_pm_up = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_up['left'] = fuzz.trimf(next_move_pm_up.universe,[0,25, 50])
        next_move_pm_up['up'] = fuzz.trimf(next_move_pm_up.universe,[25,50,75])
        next_move_pm_up['down'] = fuzz.trimf(next_move_pm_up.universe, [50,75,100])
        food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Angle is based on the 4 quadrant'''

        food_loc['up'] = fuzz.trimf(food_loc.universe,[-90,0, 90])
        food_loc['left'] = fuzz.trimf(food_loc.universe,[45,135,180])
        food_loc['right'] = fuzz.trimf(food_loc.universe, [-180,-135,-45])

    def mf_pm_down(self):
        '''if the previous move is DOWN, the only direciton
        you can move is DOWN, LEFT, RIGHT'''
        next_move_pm_down = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_down['left'] = fuzz.trimf(next_move_pm_down.universe,[0,25, 50])
        next_move_pm_down['down'] = fuzz.trimf(next_move_pm_down.universe,[25,50,75])
        next_move_pm_down['right'] = fuzz.trimf(next_move_pm_down.universe,[50,75,100])

        #Brick Location
        food_loc = ctrl.Antecedent(np.arange(-180, 181, 1), 'food_loc')
        '''Angle is based on the 4 quadrant'''

        food_loc['up'] = fuzz.trimf(food_loc.universe,[-90,0, 90])
        food_loc['left'] = fuzz.trimf(food_loc.universe,[45,135,180])
        food_loc['right'] = fuzz.trimf(food_loc.universe, [-180,-135,-45])

    def get_angle(food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
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
            # m.degress(m.atan2((food.y-snake.y[0]),(food.x -snake.x[0])))


        # m.degress(m.atan2((food.y-snake.y[0]),(food.x -snake.x[0])))


    def perform_next_move(self, snake, food, bricks):
        if self.current_move_number < self.max_moves:
            if snake.direction == constants.RIGHT:
                self.mf_pm_right()

                rule1 = ctrl.Rule(mf_pm_right.food_loc['up'], next_move['up'])
                rule2 = ctrl.Rule(mf_pm_right.food_loc['left'], next_move['left'])
                rule3 = ctrl.Rule(mf_pm_right.food_loc['right'], next_move['right'])

                angle = get_angle(food.y, food.x, snake.y[0], snake.x[0])
                next_move_crtl = ctrl.ControlSystem([rule1, rule2, rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)

                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                if result < 3:
                    snake.moveUp()
                if result >=3 and result <=7:
                    snake.moveRight()
                else:
                    snake.moveDown()
            if snake.direction == constants.LEFT:
                self.mf_pm_left()

                rule1 = ctrl.Rule(food_loc['up'], next_move['up'])
                rule2 = ctrl.Rule(food_loc['left'], next_move['left'])
                rule3 = ctrl.Rule(food_loc['down'], next_move['down'])

                angle = get_angle(food.y, food.x, snake.y[0], snake.x[0])
                next_move_crtl = ctrl.ControlSystem([rule1, rule2, rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)

                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                if result < 3:
                    snake.moveUp()
                if result >=3 and result <=7:
                    snake.moveLeft()
                else:
                    snake.moveDown()

            if snake.direction == constants.UP:
                self.mf_pm_Up()

                rule1 = ctrl.Rule(food_loc['left'], next_move['left'])
                rule2 = ctrl.Rule(food_loc['up'], next_move['up'])
                rule3 = ctrl.Rule(food_loc['down'], next_move['down'])

                angle = get_angle(food.y, food.x, snake.y[0], snake.x[0])
                next_move_crtl = ctrl.ControlSystem([rule1, rule2, rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)

                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                if result < 3:
                    snake.moveLeft()
                if result >=3 and result <=7:
                    snake.moveUp()
                else:
                    snake.moveDown()
            if snake.direction == constants.DOWN:
                self.mf_pm_Down()

                rule1 = ctrl.Rule(food_loc['up'], next_move['up'])
                rule2 = ctrl.Rule(food_loc['left'], next_move['left'])
                rule3 = ctrl.Rule(food_loc['right'], next_move['right'])

                angle = get_angle(food.y, food.x, snake.y[0], snake.x[0])
                next_move_crtl = ctrl.ControlSystem([rule1, rule2, rule3])
                next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)

                next_move_crtl_fuzzy.input['food_loc'] = angle
                result = next_move_crtl_fuzzy.compute()
                if result < 3:
                    snake.moveUp()
                if result >=3 and result <=7:
                    snake.moveLeft()
                else:
                    snake.moveDown()

            # if (next_move_crtl_fuzzy.output['score'])

            #Propose 1 fuzzy system for each direction
            # if self.direction == constants.RIGHT:


            # Fuzzy rules to be put here!

            self.current_move_number += 1
            return snake, True
        return snake, False
