from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.coordinates.coordinate import Coordinate

class GameBoardSquareCollection: 
    def __init__(self):
        self.squares = {}
    
    def has(self, coord: Coordinate) -> bool:
        return coord.stringify() in self.squares
            
    def get(self, coord: Coordinate):
        return self.squares[coord.stringify()] if self.has(coord) else False
    
    def set(self, gameboardsquare: GameBoardSquare):
        key = gameboardsquare.get_coordinates().stringify()
        self.squares[key] = gameboardsquare
        
    def get_all(self) -> dict:
        return self.squares

    def get_keys(self) -> list:
        return self.squares.keys()
                
    def get_coordinates(self) -> list:
        coordinates = []
        for square in self.squares:
           coordinates.append(self.squares[square].get_coordinates())
        return coordinates
         