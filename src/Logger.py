import constants
import os

class Logger:
    def __init__(self):
        self._snake_moves_log_location = os.path.join("logs", constants.SNAKE_MOVES_FILE)

    def start_logging_new_game(self):
        with open(self._snake_moves_log_location, "a") as fa:
            fa.write("New game" + "\n")

    def log_snake_move(self, move_direction):
        move_direction_text = constants.move_direction_text_dict[move_direction]
        with open(self._snake_moves_log_location, "a") as fa:
            fa.write(move_direction_text + "\n")
