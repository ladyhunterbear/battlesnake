from .lib.gameboard import GameBoard, GameBoardSquare, GameBoardSquareState
from .lib.coordinate import Coordinate
from .lib.snake import Snake

'''
Game loads.
Generate a model of the current gameboard with food, hazards, snakes, and self.
For each snake, determine the possible moves and note those on the game square as states
For my snake, determine the best of the max 3 possible (can) moves to perform base on:
    (v1) 
        Random.
        Use rewards instead for reinforcement learning
        - food reward plus 1
        - kill reward plus 100
        - die negative reward minus 1000000
'''

class PossibleGameBoardSquare(GameBoardSquare):
    i_can = None
    move_score = 0 # this is the should score
    someone_can = None
    weight_nearest_food = -1 #should be calc based on health
    weight_nearest_enemy = -1
    nearest_snake = -1
    nearest_food = -1
    my_weight = 0
    everyones_weight = 0

    def is_available(self):
        return False

    def will_be_available(self):
        return False

    def might_be_avialable(self):
        return False

    def get_move_score(self):
        return self.move_score
        

class Turn:
    gameboard = None

    def __init__( self, request ):
        