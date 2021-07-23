from battlesnake2.lib.coordinates.coordinate import Coordinate
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.enums.directions import Direction
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.gameboard.gameboardsquarecollection import GameBoardSquareCollection
from battlesnake2.lib.strategies.gamestrategyfactory import GameStrategyFactory
from battlesnake2.lib.strategies.gamestrategy import GameStrategy
from battlesnake2.lib.request.requestreader import RequestReader
from battlesnake2.lib.snakes.snakesquares import SnakeSquares
from typing import Union, List
from random import *

'''
A default Game brain.
All the business logic for creating the board and handling the game.

Move all logic here and out of the other classes.
'''
class Game:
    state: GameState
    strategy: GameStrategy
    
    '''
    Initialize the game by setting the game board condition
    '''
    def __init__(self, request: object):
        # Setup the game board
        self.setup_gameboard(request)
        # Set the strategy based on the game mode
        self.set_strategy()
    
    
    def setup_gameboard(self, request: object):
        # create a request reader to parse the json request object
        request = RequestReader(request)
        # create a state object to store game properties
        self.state = GameState()
        # create the game board
        self.state.set_gameboard(request.gameboard())
        # add my snake
        self.state.set_my_snake(request.my_snake())
        self.add_my_snake_squares()
        # add opponents
        self.state.set_opponents(request.opponents())
        if self.state.get_opponents().count() > 0:
            self.add_opponent_snake_squares()
        # add food
        self.state.set_food(request.food())
        self.add_to_gameboard(self.state.get_food())
        # add hazards
        self.state.set_hazards(request.hazards())
        self.add_to_gameboard(self.state.get_hazards())
        # specify ruleset
        self.state.set_ruleset(request.ruleset())
        
    def add_opponent_snake_squares(self):
        opponents = self.state.get_opponents()
        for id in opponents.get_ids():
            snake_squares = SnakeSquares(self.state.get_my_snake(), opponents.get(id))
            self.add_to_gameboard(snake_squares.get_squares())
        
    def add_my_snake_squares(self):
        snake_squares = SnakeSquares(self.state.get_my_snake())
        self.add_to_gameboard(snake_squares.get_squares())

    def add_to_gameboard(self, square_collection: GameBoardSquareCollection):
        gameboard = self.state.get_gameboard()
        squares = square_collection.get_all()
        for key in squares:
            gameboard.set_square(squares[key])
        self.state.set_gameboard(gameboard)
         
    def set_strategy(self) -> GameStrategy:
        game_strategy_factory = GameStrategyFactory()
        self.strategy = game_strategy_factory.make(self.state)
    
    # def get_next_move_score(self, coord: Coordinate) -> float:
    #     max_move_score = 300 # total of highest possible scoring moves (food)
    #     next_move_score = 0
    #     possible_next_moves = self.gameboard.get_possible_directions(coord)
    #     for direction in possible_next_moves:
    #         next_move_score = next_move_score + self.gameboard.get_square(possible_next_moves[direction]).get_state_value()
    #     return next_move_score / max_move_score
    #     
    #     

    def relative_direction(self, origin: Coordinate, destination: Coordinate) -> str:
        direction = ''
        if destination.get_y() == origin.get_y() and destination.get_x() > origin.get_x():
            direction = 'right'
        elif destination.get_y() == origin.get_y() and destination.get_x() < origin.get_x():
            direction = 'left'
        elif destination.get_y() > origin.get_y() and destination.get_x() == origin.get_x():
            direction = 'up'
        elif destination.get_y() < origin.get_y() and destination.get_x() == origin.get_x():
            direction = 'down'
        else:
            direction = 'invalid'
        return direction
        
    '''
    Evaluate the game board
    '''
    def evaluate_gameboard(self):
        best_move_coords = None
        best_move_score = 0
        gameboard = self.state.get_gameboard()
        # Strategies
        gameboard = self.strategy.process(gameboard, self.state);
        
        my_possible_moves = gameboard.get_adjacent_coordinates(self.state.get_my_snake().get_head())
        for coords in my_possible_moves:
            best_move_score = best_move_score + random()
            new_square_score = gameboard.get_square(coords).get_state().value + random()
            if new_square_score > best_move_score:
                best_move_score = gameboard.get_square(coords).get_state().value
                best_move_coords = coords
        return self.relative_direction(self.state.get_my_snake().get_head(), best_move_coords)
    
    '''
    Main method for processing and returning game move
    '''
    def get_move(self):
        choice = self.evaluate_gameboard()
        board_matrix = self.state.get_gameboard().get_board_matrix()
        # print(board_matrix)
        # print(choice)        
        return {"move": choice, "shout": str("I should move " + choice)}