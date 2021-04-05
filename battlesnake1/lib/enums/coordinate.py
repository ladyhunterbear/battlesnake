class Coordinate:
    x: int
    y: int
    
    def set_x(self, x):
        self.x = x
    
    def get_x(self) -> int:
        return self.x
        
    def set_y(self, y):
        self.y = y

    def get_y(self) -> int:
        return self.y
    
    def stringify(self) -> str:
        return str(self.x) + "_" + str(self.y)
    
    def __init__(self, x, y):
        self.x = x
        self.y = y