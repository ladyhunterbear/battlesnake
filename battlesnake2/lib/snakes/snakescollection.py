from battlesnake2.lib.snakes.snake import Snake

class SnakesCollection:  
    def __init__(self):
        self.snakes = {}
  
    def set(self, snake: Snake):
        self.snakes[snake.get_id()] = snake
    
    def get(self, id):
        return self.snakes[id] if id in self.snakes.keys() else False
    
    def get_ids(self):
        return self.snakes.keys()
        
    def empty(self):
        return len(self.snakes) == 0
        
    def count(self):
        return len(self.snakes)
    
    '''
    Returns the length of the longest opponent snake in the collection.
    '''
    def get_longest_length(self) -> int:
        max_snake_length = 0
        for snake_id in self.get_ids():
            snake = self.get(snake_id)
            if snake and snake.is_alive() and snake.get_length() > max_snake_length:
                max_snake_length = snake.get_length() + 1 
        
        return max_snake_length  
  
  
    '''
    Define reverse lookup for snake id by square coordinate.
    '''
    def add_snake_to_snake_square_lookup(self, square_coordinate, snake_id):
        self.snake_squares[square_coordinate] = snake_id
      

  
  