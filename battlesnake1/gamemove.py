from battlesnake1.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake1.lib.strategies.gathererstrategy import GathererStrategy
from battlesnake1.lib.strategies.hunterstrategy import HunterStrategy
from battlesnake1.lib.strategies.wandererstrategy import WandererStrategy
from battlesnake1.lib.strategies.circularstrategy import CircularStrategy
from battlesnake1.lib.strategies.avoidancestrategy import AvoidanceStrategy
from battlesnake1.lib.strategies.protectionstrategy import ProtectionStrategy
from battlesnake1.gameboardsquare import GameBoardSquare
from battlesnake1.gameboard import GameBoard
from battlesnake1.lib.enums.coordinate import Coordinate
from battlesnake1.lib.enums.directions import Direction
from battlesnake1.snake import Snake
from typing import Union, List
from random import *
'''
A default Game brain.
All the business logic for creating the board and handling the game.

Move all logic here and out of the other classes.
'''
class Game:
    gameboard: GameBoard = None
    snakes = {}
    my_snake = None
    snake_squares = {}
    

    '''
    Initialize the game by setting the game board condition
    '''
    def __init__(self, request):
        self.gameboard = GameBoard(request)
        self.add_hazards(request['board']['hazards'])
        self.add_my_snake(request['you'])
        self.add_snakes(request['board']['snakes'])
        self.add_food(request['board']['food'])

    '''
    Get snake by snake ID
    '''
    def get_snake_by_id(self, id):
        for snake_id in self.snakes:
            if snake_id == id:
                return self.snakes[snake_id]
        return False

    


    def evaluate_gameboard(self):
        choice = 'up'
        choice_score = 0
        best_move_coords = None
        best_move_score = 0
        
        # Strategies
        
        # Wander Strategy
        wanderer_strategy = WandererStrategy()
        self.gameboard = wanderer_strategy.process(self.gameboard)
        
        # Protection Strategy
        protection_strategy = ProtectionStrategy()
        self.gameboard = protection_strategy.process(self.gameboard)
        
        # Gatherer Strategy
        max_snake_length = len(self.gameboard.squares) * 0.25
        if (self.my_snake.get_health() < 50 or self.my_snake.get_length() < max_snake_length):
            gatherer_strategy = GathererStrategy()
            self.gameboard = gatherer_strategy.process(self.gameboard)
        
        #Avoidance Strategy
        avoidance_strategy = AvoidanceStrategy()
        self.gameboard = avoidance_strategy.process(self.gameboard)
        
        # Hunter Strategy
        hunter_strategy = HunterStrategy()
        self.gameboard = hunter_strategy.process(self.gameboard)
        
        
        
        
        my_possible_moves = self.gameboard.get_possible_directions(self.my_snake.get_head())
        if (my_possible_moves):
            for direction in my_possible_moves:
                seed_A = random()
                seed_B = random()
                possible_move_coords = my_possible_moves[direction]
                possible_move_square = self.gameboard.get_square(possible_move_coords)
                possible_moves_score = possible_move_square.get_state_value() + seed_A
                possible_best_move_score = best_move_score + seed_B
                if  possible_moves_score > possible_best_move_score:
                    best_move_coords = possible_move_coords
                    best_move_score = possible_move_square.get_state_value()
                    choice = direction


        return choice


    '''
    Add my snake to the game board
    '''
    def add_my_snake(self, you):
        self.my_snake = Snake(you)
        for body_coords in self.my_snake.body:
            coord = Coordinate(self.my_snake.body[body_coords].get_x(), self.my_snake.body[body_coords].get_y())
            square = self.gameboard.get_square(coord)
            square.set_state(GameBoardSquareState.SNAKE_SELF_BODY)
        head_coord = Coordinate(self.my_snake.get_head().get_x(), self.my_snake.get_head().get_y())
        head_square = self.gameboard.get_square(head_coord)
        head_square.set_state(GameBoardSquareState.SNAKE_SELF_HEAD)
    
    
    '''
    Add food to the game board.
    '''
    def add_food(self, food_squares):
        if (len(food_squares)):
            for food in food_squares:
                coord = Coordinate(food['x'], food['y'])
                square = self.gameboard.get_square(coord).set_state(GameBoardSquareState.FOOD)
    
    '''
    Add enemy snakes to the game board.
    '''
    def add_snakes(self, snakes):
        for enemy_snake in snakes:
            if (enemy_snake['id'] != self.my_snake.get_id()):
                snake = Snake(enemy_snake)
                self.snakes[snake.id] = snake
                for body_coords in snake.body:
                    coord = Coordinate(snake.body[body_coords].get_x(), snake.body[body_coords].get_y())
                    self.gameboard.get_square(coord).set_state(GameBoardSquareState.SNAKE_ENEMY_BODY)
                    self.add_snake_to_snake_square_lookup(coord, snake.id)
                snake_head_coord = Coordinate(snake.get_head().get_x(), snake.get_head().get_y())
                head_square = self.gameboard.get_square(snake_head_coord)
                
                if self.enemy_snake_is_weaker(snake):
                    head_square.set_state(GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD)
                
                if self.enemy_snake_is_equal(snake):
                    head_square.set_state(GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD)
                
                if self.enemy_snake_is_stronger(snake):
                    head_square.set_state(GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD)


    '''
    Check if enemy snake is weaker.
    '''
    def enemy_snake_is_weaker(self, enemy_snake) -> bool:
        return True if enemy_snake.get_length() < self.my_snake.get_length() else False
        
    '''
    Check if enemy snake is equal in health.
    '''
    def enemy_snake_is_equal(self, enemy_snake) -> bool:
        return True if enemy_snake.get_length() == self.my_snake.get_length() else False
    
    '''
    Check if enemy snake has more health than my snake
    '''
    def enemy_snake_is_stronger(self, enemy_snake) -> bool:
        return True if enemy_snake.get_length() > self.my_snake.get_length() else False
    

    '''
    Define reverse lookup for snake id by square coordinate.
    '''
    def add_snake_to_snake_square_lookup(self, square_coordinate, snake_id):
        self.snake_squares[square_coordinate] = snake_id

    '''
    Add hazards to game board.
    '''
    def add_hazards(self, hazards):
        if (len(hazards)):
            for hazard in hazards:
                hazard_coord = Coordinate(hazard['x'], hazard['y'])
                self.gameboard.get_square(hazard_coord).set_state(GameBoardSquareState.HAZARD)


    def get_move(self):        
        choice = self.evaluate_gameboard()
        board_matrix = self.gameboard.get_board_matrix()
        # print(board_matrix)
        # print(choice)
        response = {"move": choice, "shout": "I should move " + choice}    
        return response
