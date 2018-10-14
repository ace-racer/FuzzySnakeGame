from Game import Game
import constants
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import math as m


class FuzzyRulesForBricksController:


    def __init__(self, max_moves=2000):
        pass



    def perform_next_move(self, snake, food, bricks):
        print("Fuzzy with bricks")
        return snake, True



