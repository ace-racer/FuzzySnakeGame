# Overview

There are 2 parameters that the Snake game we have developed takes as inputs – the type of controller that is used to control the snake and the layout of obstacles that the snake needs to maneuver in the game arena. These parameters are described in detail below. We then describe the steps to install the dependencies requires to execute the application and then finally how to run after installing the dependencies.

# Snake controllers

0. Manual controller - When the application is run with the controller specified as 0, then the snake is controlled by the manual press of up, down, left and right keys.
1.	Crisp rules controller – When the snake is run with the controller specified as 1, then the crisp rules controller controls the snake. This is the baseline controller for all comparisons performed in the report.
2.	Fuzzy rules controller – When the snake is run with the controller specified as 2, then the tuned Fuzzy rules defined controller is used to control the snake.
3.	Fuzzy rules controller for bricks – When the snake is run with the controller as 3, then the Fuzzy rules are optimized such that the snake is better able to prevent collisions with bricks present in the arena.

# Snake levels

0.	No bricks level – When the level is specified as 0 there are no bricks present in the arena and the only way for the snake to die is a self-collision. This is the simplest level for the snake to maneuver.
 
1.	Vertical bricks level – When the level is specified as 1 the bricks are laid out in a vertical pattern. If the snake collides with any brick in the brick wall, then it would perish and the game will be over.
 

2.	Horizontal bricks level – When the level is specified as 2, the bricks are laid out in a horizontal pattern. The difficult of this level is the same as that of the earlier level.
 
3.	L shaped bricks level – When the level is specified as 3, the bricks are laid out in an inverted L shaped pattern. This is the most difficult level for the snake to maneuver.
 
# Installation of dependencies

## Pre-requisites
* Python 3.6 or above
* Anaconda version 5.1.0 or above 
* Windows OS
* Visual Studio C++ build tools to install scikit-fuzzy
* Latest pip installer

## Installation process
* Navigate into the Snake game source code (src folder)
* Open a command prompt in the Administrator mode
* Create a conda environment called “fuzzygame”
* > conda create --name fuzzygame python=3.6
* > activate fuzzygame
* Find the requirements.txt file in the Snake game source code 
* > pip install -r requirements.txt 
If the installation of the dependencies from the requirements.txt fails due to some reason, please install the packages mentioned in the requirements.txt using pip in the conda environment.

# Sample runs

1.	To run the snake game with the fuzzy controller and no bricks level the game needs to be invoked in the following way:
python App.py 2 0

Here, 2 specifies the Fuzzy controller and 0 specifies the no bricks level as mentioned in the earlier sections.

2.	To run the snake game with the fuzzy bricks controller and the L bricks level the command is as below:
Python App.py 3 3

Here, the first 3 specifies the fuzzy bricks controller and the second 3 specifies the L shaped bricks layout as mentioned in the earlier sections.

Note: The Escape key can be pressed to stop the game execution at any time.

# Complete Working game demo

Please find the working game demo [here](https://drive.google.com/file/d/1SchB4zRxcKR1DHUz2TBK58dObao6Er09/view?usp=sharing)

# References

Basic game source code taken from here: https://pythonspot.com/snake-with-pygame/