# import different controllers
from snake_controllers.FuzzyRulesController import FuzzyRulesController
from snake_controllers.ManualController import ManualController
from snake_controllers.RuleBasedController import RuleBasedController

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
SNAKE_MOVES_FILE = "snake_moves.txt"
MANUAL = 0
RULE_BASED = 1
FUZZY = 2

move_direction_text_dict = { UP: "UP", DOWN: "DOWN", LEFT: "LEFT", RIGHT: "RIGHT"}
controller_name_mapping = { MANUAL: ManualController, RULE_BASED : RuleBasedController, FUZZY: FuzzyRulesController}
MAX_VAL = 99999
STEP_SIZE = 44