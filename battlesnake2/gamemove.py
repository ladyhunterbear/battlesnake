from battlesnake2.lib.enums.directions import Direction


class GameMove:
    move: Direction
    shout: str
  
  
    def __init__(self, direction: Direction, shout: str = 'Hisssssss...'):
        self.move = direction
        self.shout = shout
        
    
    def move() -> Direction:
        return self.move
        
        
    def shout() -> str:
        return self.shout
        
    
    def game_move() -> object: 
        return { "move": self.move, "shout": self.shout }
