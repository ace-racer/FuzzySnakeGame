from Game import Game
import constants
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import math as m


#To Calculate the angle between 2 points

#myradians = math.atan2(targetY-gunY, targetX-gunX)

class FuzzyRulesController:


    def __init__(self, max_moves=2000):
        self.max_moves = max_moves
        self.current_move_number = 0
        self.game = Game()
        self.mf_pm_right()
        self.mf_pm_left()
        self.mf_pm_up()
        self.mf_pm_down()
        self.old_snake_pos_y = 0
        self.old_snake_pos_x = 0


    def mf_pm_right(self):
        '''if the previous move is RIGHT, the only direciton
        you can move is UP, RIGHT, DOWN'''
        self.next_move_pm_right = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_right['up'] = fuzz.trimf(self.next_move_pm_right.universe,[0,25, 50])
        self.next_move_pm_right['right'] = fuzz.trimf(self.next_move_pm_right.universe,[25,50,75])
        self.next_move_pm_right['down'] = fuzz.trimf(self.next_move_pm_right.universe,[50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-181, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['right'] = fuzz.trapmf(self.food_loc.universe,[45,135,181,181])
        self.food_loc['left'] = fuzz.trapmf(self.food_loc.universe, [-181,-181,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_right['right'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_right['up'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_right['down'])

        self.collison_ang = ctrl.Antecedent(np.arange(-181, 181, 1), 'collison_ang')
        '''Based on a clock with respect the the snake head'''
        self.collison_ang['0'] = fuzz.trapmf(self.collison_ang.universe,[-90,-45,45,90])
        self.collison_ang['90'] = fuzz.trimf(self.collison_ang.universe,[45,90,135])
        self.collison_ang['-90'] = fuzz.trimf(self.collison_ang.universe, [-135,-90,-45])

        self.rule4 = ctrl.Rule(self.collison_ang['0'], self.next_move_pm_right['up'])
        self.rule5 = ctrl.Rule(self.collison_ang['90'], self.next_move_pm_right['up'])
        self.rule6 = ctrl.Rule(self.collison_ang['-90'], self.next_move_pm_right['down'])


    def mf_pm_left(self):
        '''if the previous move is LEFT, the only direciton
        you can move is UP, LEFT, DOWN'''
        self.next_move_pm_left = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_left['up'] = fuzz.trimf(self.next_move_pm_left.universe,[0,25, 50])
        self.next_move_pm_left['left'] = fuzz.trimf(self.next_move_pm_left.universe,[25,50,75])
        self.next_move_pm_left['down'] = fuzz.trimf(self.next_move_pm_left.universe,[50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-181, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['right'] = fuzz.trapmf(self.food_loc.universe,[45,135,181,181])
        self.food_loc['left'] = fuzz.trapmf(self.food_loc.universe, [-181,-181,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_left['left'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_left['down'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_left['up'])

        self.collison_ang = ctrl.Antecedent(np.arange(-181, 181, 1), 'collison_ang')
        '''Based on a clock with respect the the snake head'''
        self.collison_ang['0'] = fuzz.trapmf(self.collison_ang.universe,[-90,-45,45,90])
        self.collison_ang['90'] = fuzz.trimf(self.collison_ang.universe,[45,90,135])
        self.collison_ang['-90'] = fuzz.trimf(self.collison_ang.universe, [-135,-90,-45])

        self.rule4 = ctrl.Rule(self.collison_ang['0'], self.next_move_pm_left['up'])
        self.rule5 = ctrl.Rule(self.collison_ang['90'], self.next_move_pm_left['down'])
        self.rule6 = ctrl.Rule(self.collison_ang['-90'], self.next_move_pm_left['up'])


    def mf_pm_up(self):
        '''if the previous move is UP, the only direciton
        you can move is UP, LEFT, RIGHT'''
        self.next_move_pm_up = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_up['left'] = fuzz.trimf(self.next_move_pm_up.universe,[0,25, 50])
        self.next_move_pm_up['up'] = fuzz.trimf(self.next_move_pm_up.universe,[25,50,75])
        self.next_move_pm_up['right'] = fuzz.trimf(self.next_move_pm_up.universe, [50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-181, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['right'] = fuzz.trapmf(self.food_loc.universe,[45,135,181,181])
        self.food_loc['left'] = fuzz.trapmf(self.food_loc.universe, [-181,-181,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_up['up'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_up['left'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_up['right'])

        self.collison_ang = ctrl.Antecedent(np.arange(-181, 181, 1), 'collison_ang')
        '''Based on a clock with respect the the snake head'''
        self.collison_ang['0'] = fuzz.trapmf(self.collison_ang.universe,[-90,-45,45,90])
        self.collison_ang['90'] = fuzz.trimf(self.collison_ang.universe,[45,90,135])
        self.collison_ang['-90'] = fuzz.trimf(self.collison_ang.universe, [-135,-90,-45])

        self.rule4 = ctrl.Rule(self.collison_ang['0'], self.next_move_pm_up['left'])
        self.rule5 = ctrl.Rule(self.collison_ang['90'], self.next_move_pm_up['left'])
        self.rule6 = ctrl.Rule(self.collison_ang['-90'], self.next_move_pm_up['right'])
    #
    def mf_pm_down(self):
        '''if the previous move is DOWN, the only direciton
        you can move is DOWN, LEFT, RIGHT'''
        self.next_move_pm_down = ctrl.Consequent(np.arange(0, 101, 1), 'Next Direction')
        self.next_move_pm_down['left'] = fuzz.trimf(self.next_move_pm_down.universe,[0,25, 50])
        self.next_move_pm_down['down'] = fuzz.trimf(self.next_move_pm_down.universe,[25,50,75])
        self.next_move_pm_down['right'] = fuzz.trimf(self.next_move_pm_down.universe,[50,75,100])

        self.food_loc = ctrl.Antecedent(np.arange(-181, 181, 1), 'food_loc')
        '''Based on a clock with respect the the snake head'''
        self.food_loc['up'] = fuzz.trimf(self.food_loc.universe,[-90,0, 90])
        self.food_loc['right'] = fuzz.trapmf(self.food_loc.universe,[45,135,181,181])
        self.food_loc['left'] = fuzz.trapmf(self.food_loc.universe, [-181,-181,-135,-45])

        self.rule1 = ctrl.Rule(self.food_loc['up'], self.next_move_pm_down['down'])
        self.rule2 = ctrl.Rule(self.food_loc['left'], self.next_move_pm_down['right'])
        self.rule3 = ctrl.Rule(self.food_loc['right'], self.next_move_pm_down['left'])

        self.collison_ang_1 = ctrl.Antecedent(np.arange(-181, 181, 1), 'collison_ang')
        '''Based on a clock with respect the the snake head'''
        self.collison_ang['0'] = fuzz.trapmf(self.collison_ang.universe,[-90,-45,45,90])
        self.collison_ang['90'] = fuzz.trimf(self.collison_ang.universe,[45,90,135])
        self.collison_ang['-90'] = fuzz.trimf(self.collison_ang.universe, [-135,-90,-45])

        self.rule4 = ctrl.Rule(self.collison_ang['0'], self.next_move_pm_down['left'])
        self.rule5 = ctrl.Rule(self.collison_ang['90'], self.next_move_pm_down['right'])
        self.rule6 = ctrl.Rule(self.collison_ang['-90'], self.next_move_pm_down['left'])


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
            final_angle = -(180-angle)
        if angle >= 90 and angle <= 180:
            final_angle = -(180-angle)
        if  -90 <=angle <= 0:
            final_angle = 180 + angle
        if angle >= -180 and angle <= -90:
            final_angle = 180 + angle
        return int(final_angle)

    def get_angle_pm_up(self,food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
        print(str(food_y) + " " + str(food_x) + " " + str(snake_y) +" " + str(snake_x))
        angle = m.degrees(m.atan2((food_y-snake_y),(food_x - snake_x)))
        if angle <= 90 and angle >= 0:
            final_angle = 90 + angle
        if angle >= 90 and angle <= 180:
            final_angle = (angle - 90)-180
        if  -90 <=angle <= 0:
            final_angle = 90 + angle
        if angle >= -180 and angle <= -90:
            final_angle = angle + 90
        return int(final_angle)

    def get_angle_pm_down(self,food_y, food_x, snake_y,snake_x):
        '''Angle is based on the 4 quadrant
        We require to convert it back where 0 is the y-axis'''
        print(str(food_y) + " " + str(food_x) + " " + str(snake_y) +" " + str(snake_x))
        angle = m.degrees(m.atan2((food_y-snake_y),(food_x - snake_x)))
        if angle <= 90 and angle >= 0:
            final_angle = -(90 - angle)
        if angle >= 90 and angle <= 180:
            final_angle = angle - 90
        if  -90 <=angle <= 0:
            final_angle = angle-90
        if angle >= -180 and angle <= -90:
            final_angle = 270+angle
        return int(final_angle)

    #Calculate Mahatten Distance
    #Put in a list of x and y values
    def manhatten_distance(self, snake_x , snake_y):
        overall_man_dist = []
        for i in range(0,len(snake_x)):
            x_head = snake_x[0]
            y_head = snake_y[0]
            manhatten_distance = int((abs(x_head - snake_x[i]) + abs(y_head - snake_y[i]))/44)
            overall_man_dist.append(manhatten_distance)
        return overall_man_dist


    def check_snake(self,snake_x , snake_y):
        length_of_snake = len(snake_x)
        if snake_x[-1] == -100:
            snake_x.pop()
            snake_y.pop()
        else:
            pass
        return snake_x,snake_y


    def perform_next_move(self, snake, food, bricks):
        overall_rules = []
        indicator = 0
        if self.current_move_number < self.max_moves:
            if self.old_snake_pos_y ==  snake.y[0] and self.old_snake_pos_x == snake.x[0] and self.current_move_number != 0:
                if snake.direction == constants.LEFT:
                    snake.moveLeft()
                if snake.direction == constants.RIGHT:
                    snake.moveRight()
                if snake.direction == constants.UP:
                    snake.moveUp()
                if snake.direction == constants.DOWN:
                    snake.moveDown()
                self.current_move_number += 1
            else:

                if snake.direction == constants.RIGHT:
                    self.mf_pm_right()
                    overall_rules = [self.rule1, self.rule2, self.rule3]

                    angle = self.get_angle_pm_right(food.y, food.x, snake.y[0], snake.x[0])
                    print("Angle :" +str(angle))

                    snake_x,snake_y = self.check_snake(snake.x[0:snake.length],snake.y[0:snake.length])
                    overall_man_dist = self.manhatten_distance(snake_x,snake_y)
                    print(overall_man_dist)
                    if snake.length > 4:
                        print("Wee")
                        for i in range(3, len(overall_man_dist)):
                            if overall_man_dist[i] == 1:
                                print('Offending parts are:' + " " +str(snake.y[0]) + " " +str(snake.x[0]) + " " +
                                        str(snake.y[i]) + " " +str(snake.x[i]))
                                collison_angle = self.get_angle_pm_right(snake.y[i], snake.x[i],snake.y[0], snake.x[0])
                                print('Collison angle is :' + str(collison_angle))
                                overall_rules.extend((self.rule4, self.rule5, self.rule6))

                                indicator = 1
                            else:
                                pass

                    next_move_crtl = ctrl.ControlSystem(overall_rules)
                    next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                    next_move_crtl_fuzzy.input['food_loc'] = angle

                    if indicator == 1:
                        next_move_crtl_fuzzy.input['collison_ang'] = collison_angle
                    else:
                        pass

                    result = next_move_crtl_fuzzy.compute()
                    result = int(next_move_crtl_fuzzy.output['Next Direction'])
                    print(str(result)+" is the output score." )
                    if result >= 0 and result < 35:
                        snake.moveUp()
                        print("Move up1")
                        print("################")
                    if result >=35 and result <=65:
                        snake.moveRight()
                        print("Move right2")
                        print("################")
                    if result >65 and result <= 100:
                        snake.moveDown()
                        print("Move down3")
                        print("################")


                elif snake.direction == constants.LEFT:
                    self.mf_pm_left()
                    overall_rules = [self.rule1, self.rule2, self.rule3]
                    angle = self.get_angle_pm_left(food.y, food.x, snake.y[0], snake.x[0])

                    print("Angle :" +str(angle))
                    snake_x,snake_y = self.check_snake(snake.x[0:snake.length],snake.y[0:snake.length])
                    overall_man_dist = self.manhatten_distance(snake_x,snake_y)
                    print(overall_man_dist)
                    if snake.length > 4:
                        print("Wee")
                        for i in range(3, len(overall_man_dist)):
                            if overall_man_dist[i] == 1:
                                print('yeah')
                                collison_angle = self.get_angle_pm_left(snake.y[i], snake.x[i],snake.y[0], snake.x[0])
                                print('Offending parts are:' + " " +str(snake.y[0]) + " " +str(snake.x[0]) + " " +
                                    str(snake.y[i]) + " " +str(snake.x[i]))
                                print('Collison angle is :' + str(collison_angle))
                                overall_rules.extend((self.rule4, self.rule5, self.rule6))

                                indicator = 1
                            else:
                                pass
                    next_move_crtl = ctrl.ControlSystem(overall_rules)
                    next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                    next_move_crtl_fuzzy.input['food_loc'] = angle



                    if indicator == 1:
                        next_move_crtl_fuzzy.input['collison_ang'] = collison_angle
                    else:
                        pass


                    result = next_move_crtl_fuzzy.compute()
                    result = int(next_move_crtl_fuzzy.output['Next Direction'])

                    print(str(result)+" is the output score." )
                    if result >= 0 and result < 35:
                        snake.moveUp()
                        print("Move up4")
                        print("################")
                    if result >=35 and result <=65:
                        snake.moveLeft()
                        print("Move Left5")
                        print("################")
                    if result >65 and result <= 100:
                        snake.moveDown()
                        print("Move Down6")
                        print("################")
                elif snake.direction == constants.UP:
                    self.mf_pm_up()
                    overall_rules = [self.rule1, self.rule2, self.rule3]
                    angle = self.get_angle_pm_up(food.y, food.x, snake.y[0], snake.x[0])

                    print("Angle :" +str(angle))

                    snake_x,snake_y = self.check_snake(snake.x[0:snake.length],snake.y[0:snake.length])
                    overall_man_dist = self.manhatten_distance(snake_x,snake_y)
                    print(overall_man_dist)
                    if snake.length > 4:
                        print("weee")
                        for i in range(3, len(overall_man_dist)):
                            if overall_man_dist[i] == 1:

                                collison_angle = self.get_angle_pm_up(snake.y[i], snake.x[i],snake.y[0], snake.x[0])
                                print('Offending parts are:' + " " +str(snake.y[0]) + " " +str(snake.x[0]) + " " +
                                    str(snake.y[i]) + " " +str(snake.x[i]))
                                print('Collison angle is :' + str(collison_angle))
                                overall_rules.extend((self.rule4, self.rule5, self.rule6))

                                indicator = 1
                            else:
                                pass
                    next_move_crtl = ctrl.ControlSystem(overall_rules)
                    next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                    next_move_crtl_fuzzy.input['food_loc'] = angle


                    if indicator == 1:
                        next_move_crtl_fuzzy.input['collison_ang'] = collison_angle
                    else:
                        pass

                    result = next_move_crtl_fuzzy.compute()
                    result = int(next_move_crtl_fuzzy.output['Next Direction'])
                    print(str(result)+" is the output score." )
                    if result >= 0 and result < 35:
                        snake.moveLeft()
                        print("Move Left7")
                        print("################")
                    if result >=35 and result <=65:
                        snake.moveUp()
                        print("Move up8")
                        print("################")
                    if result >65 and result <= 100:
                        snake.moveRight()
                        print("Move Right9")
                        print("################")


                elif snake.direction == constants.DOWN:
                    self.mf_pm_down()
                    overall_rules = [self.rule1, self.rule2, self.rule3]
                    angle = self.get_angle_pm_down(food.y, food.x, snake.y[0], snake.x[0])
                    print("Angle :" +str(angle))
                    snake_x,snake_y = self.check_snake(snake.x[0:snake.length],snake.y[0:snake.length])
                    overall_man_dist = self.manhatten_distance(snake_x,snake_y)
                    print(overall_man_dist)
                    if snake.length > 4:
                        print("wee")
                        for i in range(3, len(overall_man_dist)):
                            if overall_man_dist[i] == 1:
                                collison_angle = self.get_angle_pm_down(snake.y[i], snake.x[i],snake.y[0], snake.x[0])
                                print('Offending parts are:' + " " +str(snake.y[0]) + " " +str(snake.x[0]) + " " +
                                    str(snake.y[i]) + " " +str(snake.x[i]))
                                print('Collison angle is :' + str(collison_angle))
                                overall_rules.extend((self.rule4, self.rule5, self.rule6))
                                indicator = 1
                            else:
                                pass
                    next_move_crtl = ctrl.ControlSystem(overall_rules)
                    next_move_crtl_fuzzy = ctrl.ControlSystemSimulation(next_move_crtl)
                    next_move_crtl_fuzzy.input['food_loc'] = angle


                    if indicator == 1:
                        next_move_crtl_fuzzy.input['collison_ang'] = collison_angle
                    else:
                        pass

                    result = next_move_crtl_fuzzy.compute()
                    result = int(next_move_crtl_fuzzy.output['Next Direction'])
                    print(str(result)+" is the output score." )
                    if result >= 0 and result < 35:
                        snake.moveLeft()
                        print("Move Left10")
                        print("################")
                    if result >=35 and result <=65:
                        snake.moveDown()
                        print("Move Down11")
                        print("################")
                    if result >65 and result <= 100:
                        snake.moveRight()
                        print("Move Right12")
                        print("################")

                self.old_snake_pos_y = snake.y[0]
                self.old_snake_pos_x = snake.x[0]

                self.current_move_number += 1
            return snake, True
        return snake, False




