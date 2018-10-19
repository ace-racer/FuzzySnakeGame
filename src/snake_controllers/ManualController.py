from pygame.locals import *
from random import randint
import pygame
import time

class ManualController:
    def __init__(self):
        pass

    def perform_next_move(self, snake, food, bricks):
        keys = pygame.key.get_pressed() 
 
        if (keys[K_RIGHT]):
            snake.moveRight()

        if (keys[K_LEFT]):
            snake.moveLeft()

        if (keys[K_UP]):
            snake.moveUp()

        if (keys[K_DOWN]):
            snake.moveDown()
        
        should_continue_running = True
        if (keys[K_ESCAPE]):
            should_continue_running = False

        return snake, should_continue_running