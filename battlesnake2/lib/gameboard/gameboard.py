from battlesnake2.lib.coordinates.coordinate import Coordinate
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.enums.directions import Direction
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.gameboard.gameboardsquarecollection import GameBoardSquareCollection
from battlesnake2.lib.gameboard.gameboarddirectioncollection import GameBoardDirectionCollection

from typing import Union, List
import numpy as np

'''
The Game Board. A container class for all the GameBoardSquares.
Shouldn't know anything about the rules of the game or the players on the board.
'''
class GameBoard:
    def __init__(self):
        self.board_size = 0
        self.height = 0
        self.width = 0
        self.squares: GameBoardSquareCollection = GameBoardSquareCollection()
     
    '''
    Create the game board collection of GameBoardSquares with default values based on 
    height and width of the game board.
    '''
    def initialize_gameboard_squares(self):
        self.squares = GameBoardSquareCollection()
        for col in range(self.width):
            for row in range(self.height):
                self.squares.set(GameBoardSquare(Coordinate(row, col), GameBoardSquareState.EMPTY))


    '''
    Sets the game board dimensions.
    '''
    def set_board_dimensions(self, height, width):
        self.height = height
        self.width = width
        self.board_size = height * width
        
        
    def get_board_dimensions(self) -> tuple:
        return (self.height, self.width)
        
        
    '''
    Get game board square if it exists
    '''
    def get_square(self, coordinate: Coordinate):
        return self.squares.get(coordinate)

    '''
    Set game board square
    '''
    def set_square(self, square: GameBoardSquare):
        if self.in_gameboard_bounds(square.get_coordinates()):
            self.squares.set(square)
 
    def get_squares(self) -> GameBoardSquareCollection:
        return self.squares
 
    '''
    Determines if provided coordinates are within the game board bounds.
    '''
    def in_gameboard_bounds(self, coord: Coordinate) -> bool:
        x = coord.get_x()
        y = coord.get_y()
        return x >= 0 and x < self.width and y >= 0 and y < self.height
    
    '''
    Returns the game board as a NumPy array of GameBoardSquare.scores.
    '''
    def get_board_matrix(self):
        rows = []
        for i in range(self.height):
            rows.append([])
            for j in range(self.width):
                rows[i].append(self.squares.get(Coordinate(j, i)).get_state_value())
        rows.reverse()        
        board_matrix = np.array(rows)
        return board_matrix

    '''
    Gets the next Coordinate from a given point in the provided Direction
    '''
    def get_adjacent_square_coordinates(self, coord: Coordinate, dir: Direction):
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
    Generates a GameBoardSquareCollection of GameBoardSquares within the game board bounds 
    that are vertically or horizontally adjacent to the given coordinates.
    '''
    def get_adjacent_squares(self, coord: Coordinate) -> GameBoardSquareCollection:
        adjacent_squares = GameBoardSquareCollection()
        directions = {}
        directions['up'] = Coordinate(coord.get_x(), coord.get_y() + 1)
        directions['right'] = Coordinate(coord.get_x() + 1, coord.get_y())
        directions['down'] = Coordinate(coord.get_x(), coord.get_y() - 1)
        directions['left'] = Coordinate(coord.get_x() - 1, coord.get_y())
        for direction in directions:
            if self.in_gameboard_bounds(directions[direction]):
                adjacent_squares.set(self.squares.get(coord))
        return adjacent_squares
        
    def get_adjacent_coordinates(self, coord: Coordinate) -> list:
        adjacent_square_coords = [];
        up = Coordinate(coord.get_x(), coord.get_y() + 1)
        if self.in_gameboard_bounds(up):
            adjacent_square_coords.append(up)
        down = Coordinate(coord.get_x() + 1, coord.get_y())
        if self.in_gameboard_bounds(down):
            adjacent_square_coords.append(down)
        left = Coordinate(coord.get_x(), coord.get_y() - 1)
        if (self.in_gameboard_bounds(left)):
            adjacent_square_coords.append(left)
        right = Coordinate(coord.get_x() - 1, coord.get_y())
        if (self.in_gameboard_bounds(right)):
            adjacent_square_coords.append(right)
        return adjacent_square_coords
        
    
    def filter_type(self, square_state: GameBoardSquareState) -> GameBoardSquareCollection:
        results = []
        for coords in self.squares.get_coordinates():
            if self.squares.get(coords).get_state() == square_state:
                results.append(coords)
        return results
            
    
    '''
    Determine if my snake can move into the specified game board square.
    '''
    def can_move(self, square_coord: Coordinate) -> bool:
        square = self.squares.get(square_coord)
        return True if square.get_state_value() > 0 else False

    
    '''
    Get squares around a given square
    '''
    def get_surrounding_squares(self, coord: Coordinate) -> GameBoardDirectionCollection:
        directions = GameBoardDirectionCollection()
        up = self.get_adjacent_square_coordinates(coord, Direction.UP)
        down = self.get_adjacent_square_coordinates(coord, Direction.DOWN)
        left = self.get_adjacent_square_coordinates(coord, Direction.LEFT)
        right = self.get_adjacent_square_coordinates(coord, Direction.RIGHT)
        if up:
            directions.set_up(up)
        if down:
            directions.set_down(down)
        if left:
            directions.set_left(left)
        if right:
            directions.set_right(right)
        return directions
        
    
    '''
    Returns a list of squares surrounding the given coordinates that are available to move into.
    '''
    def get_possible_directions(self, coord: Coordinate) -> dict:
        directions = self.get_surrounding_squares(coord)
        can_move_directions = {}
        if directions.get_up() and self.can_move(directions.get_up()):
            can_move_directions['up'] = directions.get_up()
        if directions.get_down() and self.can_move(directions.get_down()):
            can_move_directions['down'] = directions.get_down()
        if directions.get_left() and self.can_move(directions.get_left()):
            can_move_directions['left'] = directions.get_left()
        if directions.get_right() and self.can_move(directions.get_right()):
            can_move_directions['right'] = directions.get_right()
        return can_move_directions
        
        
    def distance(self, origin: Coordinate, destination: Coordinate) -> int:
        y_dist = 0
        x_dist = 0
        
        if (origin.get_y() > destination.get_y()):
            y_dist = origin.get_y() - destination.get_y()
        else:
            y_dist = destination.get_y() - origin.get_y()
            
        if (origin.get_x() > destination.get_x()):
            x_dist = origin.get_x() - destination.get_x()
        else:
            x_dist = destination.get_x() - origin.get_x()
        return x_dist + y_dist
        
        

