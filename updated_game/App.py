from pygame.locals import *
from random import randint
import pygame
import time

from Game import Game
from Food import Food
from Snake import Snake
from Bricks import Bricks
from Logger import Logger

# import different controllers
from snake_controllers.FuzzyRulesController import FuzzyRulesController
from snake_controllers.ManualController import ManualController
from snake_controllers.RuleBasedController import RuleBasedController

class App(Logger):
 
    windowWidth = 800
    windowHeight = 600
    snake = 0
    food = 0
 
    def __init__(self):
        Logger.__init__(self)
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._food_surf = None
        self._brick_image = None
        self.game = Game()
        self.snake = Snake(3, self.windowHeight, self.windowWidth) 
        self.food = Food(5,5)
        self.bricks = Bricks(10, 10)
        self._score = 0

        # this needs to be updated as required
        self.snake_controller = RuleBasedController()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("assets/snake.png").convert()
        self._food_surf = pygame.image.load("assets/food.png").convert()
        self._brick_image = pygame.image.load("assets/brick.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.snake.update()
 
        # does snake eat food?
        if self.game.isCollision(self.food.x,self.food.y,self.snake.x[0], self.snake.y[0],44):
            # add score of 1 for eating food
            self._score += 1

            self.food.x = randint(2,9) * 44
            self.food.y = randint(2,9) * 44
            self.snake.length = self.snake.length + 1
 
 
        # does snake collide with itself?
        for i in range(2,self.snake.length):
            if self.game.isCollision(self.snake.x[0],self.snake.y[0],self.snake.x[i], self.snake.y[i],40):
                print("You lose! Collision with snake: ")
                print("x[0] (" + str(self.snake.x[0]) + "," + str(self.snake.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.snake.x[i]) + "," + str(self.snake.y[i]) + ")")
                print("Your score: {0}".format(self._score))
                exit(0)

        # does snake collide with a brick?
        if self.game.isCollision(self.bricks.x,self.bricks.y, self.snake.x[0], self.snake.y[0], 40):
            print("You lose! Collision with brick: ")
            print("x[0] (" + str(self.snake.x[0]) + "," + str(self.snake.y[0]) + ")")
            print("x[" + str(i) + "] (" + str(self.bricks.x) + "," + str(self.bricks.y) + ")")
            print("Your score: {0}".format(self._score))
            exit(0)
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.snake.draw(self._display_surf, self._image_surf)
        self.food.draw(self._display_surf, self._food_surf)
        self.bricks.draw(self._display_surf, self._brick_image)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        self.start_logging_new_game()

        while( self._running ):
            pygame.event.pump()

            self.snake, should_continue_running = self.snake_controller.perform_next_move(self.snake, self.food, self.bricks)
            self.add_snake_move(self.snake.getCurrentDirection())
            self._running = should_continue_running
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0)
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()