from battlesnake2.lib.coordinates.coordinate import Coordinate
from battlesnake2.lib.enums.directions import Direction

class GameBoardDirectionCollection:
    up: Direction = None
    down: Direction = None
    left: Direction = None
    right: Direction = None
    
    
    def set_up(self, coord: Coordinate):
        self.up = coord
    
    def get_up(self):
        return self.up if type(self.up) != None else False
    
    def set_down(self, coord: Coordinate):
        self.down = coord
        
    def get_down(self):
        return self.down if type(self.down) != None else False
        
    def set_left(self, coord: Coordinate):
        self.left = coord
    
    def get_left(self):
        return self.left if type(self.left) != None else False
        
    def set_right(self, coord: Coordinate):
        self.right = coord
    
    def get_right(self):
        return self.right if type(self.right) != None else False 