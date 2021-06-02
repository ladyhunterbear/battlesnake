from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.gameboardsquare import GameBoardSquare
from battlesnake2.lib.enums.coordinate import Coordinate
from battlesnake2.lib.enums.directions import Direction
from battlesnake2.snake import Snake
from typing import Union, List
import numpy as np

'''
The Game Board. A container class for all the GameBoardSquares.
Shouldn't know anything about the rules of the game or the players on the board.
'''
class GameBoard:
    board_size = 0
    height = 0
    width = 0
    squares = {}
    
    '''
    Determines if provided coordinates are within the game board bounds.
    '''
    def in_gameboard_bounds(self, coord: Coordinate) -> bool:
        x = coord.get_x()
        y = coord.get_y()
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    '''
    Gets a GameBoardSquare from the gameboard if the key exists.
    '''
    def get_square(self, coord: Coordinate) -> Union[GameBoardSquare, bool]:
      return self.squares[coord.stringify()] if self.in_gameboard_bounds(coord) else False

    '''
    Adds a GameBoardSquare to the gameboard if coordinates are within the game board bounds.
    '''
    def add_square(self, board_square: GameBoardSquare) -> Union[GameBoardSquare, bool]:
        if self.in_gameboard_bounds(board_square.get_coordinates()):
            key = board_square.get_coordinates().stringify()
            self.squares[key] = board_square
            return self.squares[key]
        return False

    '''
    Returns the dictionary of GameBoardSquares where the key is a Coordinate.stringify()
    '''
    def get_board(self) -> List[GameBoardSquare]:
        return self.squares

    '''
    Gets the next Coordinate from a given point in the provided Direction
    '''
    def get_adjacent_square_coordinates(self, coord: Coordinate, dir: Direction) -> Union[Coordinate,bool]:
        x = coord.get_x()
        y = coord.get_y()
        if (dir == Direction.UP):
            y = y + 1
        if (dir == Direction.DOWN):
            y = y - 1
        if (dir == Direction.LEFT):
            x = x - 1
        if (dir == Direction.RIGHT):
            x = x + 1
        coord = Coordinate(x, y)
        return coord if self.in_gameboard_bounds(coord) else False

    '''
    Generates a list of GameBoardSquares within the game board bounds that are 
    vertically and horizontally adjacent to the given coordinates.
    '''
    def get_adjacent_squares(self, coord: Coordinate) -> List[GameBoardSquare]:
        squares = {}
        for direction in Directions:
            new_coord = self.get_adjacent_square(coord, Direction[direction])
            if self.in_gameboard_bounds(new_coord):
                squares[direction] = self.get_square(new_coord)
        return squares

    '''
    Returns the game board as a NumPy array of GameBoardSquare.scores.
    '''
    def get_board_matrix(self):
        rows = []
        for i in range(self.height):
            rows.append([])
            for j in range(self.width):
                key = str(j) + "_" + str(i)
                rows[i].append(self.squares[key].get_state_value())
        rows.reverse()        
        board_matrix = np.array(rows)
        return board_matrix

    '''
    Create the gameboard dictionary of GameBoardSquares with default values based on 
    height and width of the game board.
    '''
    def initialize_gameboard_squares(self):
        for col in range(self.width):
            for row in range(self.height):
                self.add_square(GameBoardSquare(Coordinate(row, col), GameBoardSquareState.EMPTY))

    '''
    Sets the game board dimensions.
    '''
    def set_board_dimensions(self, height, width):
        self.height = height
        self.width = width
        self.board_size = self.height * self.width

    '''
    Determine if my snake can move into the specified game board square.
    '''
    def can_move(self, square_coord: Coordinate) -> bool:
        square = self.get_square(square_coord)
        return True if square.get_state_value() > 0 else False

    def get_surrounding_squares(self, coord: Coordinate) -> dict:
        possible_directions = {}
        square_up_coord = self.get_adjacent_square_coordinates(coord, Direction.UP)
        square_down_coord = self.get_adjacent_square_coordinates(coord, Direction.DOWN)
        square_left_coord = self.get_adjacent_square_coordinates(coord, Direction.LEFT)
        square_right_coord = self.get_adjacent_square_coordinates(coord, Direction.RIGHT)
        
        if square_up_coord:
            possible_directions['up'] = square_up_coord
        if  square_down_coord:
            possible_directions['down'] = square_down_coord
        if  square_left_coord:
            possible_directions['left'] = square_left_coord
        if  square_right_coord:
            possible_directions['right'] = square_right_coord

        return possible_directions
        
    '''
    Returns a list of squares surrounding the given coordinates that are available to move into.
    '''
    def get_possible_directions(self, coord: Coordinate) -> dict:
        possible_directions = self.get_surrounding_squares(coord)
        can_move_directions = {}
        for direction in possible_directions:
            if self.can_move(possible_directions[direction]):
                can_move_directions[direction] = possible_directions[direction]
        return can_move_directions

    '''
    Create and initialize a new GameBoard, setting the game board height and width
    and initializing all game board squares with default values.
    '''
    def __init__(self, request):
        self.set_board_dimensions(request['board']['height'], request['board']['width'])
        self.initialize_gameboard_squares()

