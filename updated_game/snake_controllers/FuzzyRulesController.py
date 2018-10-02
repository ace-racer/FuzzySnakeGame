from Game import Game
import constants
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np



#To Calculate the angle between 2 points

#myradians = math.atan2(targetY-gunY, targetX-gunX)

class FuzzyRulesController:
    def __init__(self, max_moves=1000):
        self.max_moves = max_moves
        self.current_move_number = 0
        self.game = Game()
        self.create_memberships()

    def create_memberships(self):
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


        '''if the previous move is LEFT, the only direciton
        you can move is UP, LEFT, DOWN'''
        next_move_pm_left = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_left['up'] = fuzz.trimf(next_move_pm_left.universe,[0,25, 50])
        next_move_pm_left['left'] = fuzz.trimf(next_move_pm_left.universe,[25,50,75])
        next_move_pm_left['down'] = fuzz.trimf(next_move_pm_left.universe,[50,75,100])

        '''if the previous move is UP, the only direciton
        you can move is UP, LEFT, RIGHT'''
        next_move_pm_up = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_up['left'] = fuzz.trimf(next_move_pm_up.universe,[0,25, 50])
        next_move_pm_up['up'] = fuzz.trimf(next_move_pm_up.universe,[25,50,75])
        next_move_pm_up['down'] = fuzz.trimf(next_move_pm_up.universe, [50,75,100])

        '''if the previous move is DOWN, the only direciton
        you can move is DOWN, LEFT, RIGHT'''
        next_move_pm_down = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        next_move_pm_down['left'] = fuzz.trimf(next_move_pm_down.universe,[0,25, 50])
        next_move_pm_down['down'] = fuzz.trimf(next_move_pm_down.universe,[25,50,75])
        next_move_pm_down['right'] = fuzz.trimf(next_move_pm_down.universe,[50,75,100])

        #Brick Location
        brick_loc = ctrl.Antecedent(np.arange(0, 360, 1), 'Brick_Loc')

        brick_loc['Top_Right_Quad'] = fuzz.trimf(brick_loc.universe,[0,90, 180])
        brick_loc['Bottom_Half'] = fuzz.trapmf(brick_loc.universe,[90,150,210,270])
        brick_loc['Top_Left_Quad'] = fuzz.trimf(brick_loc.universe, [180,270,359])

        print("Membership functions added...")

    def perform_next_move(self, snake, food, bricks):
        if self.current_move_number < self.max_moves:

            #Propose 1 fuzzy system for each direction
            # if self.direction == constants.RIGHT:


            # Fuzzy rules to be put here!

            # self.current_move_number += 1
            return snake, True
        return snake, False
