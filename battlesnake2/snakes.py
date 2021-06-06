from battlesnake2.snake import Snake

class Snakes
  snakes: dict
  
  def __init__(self):
    self.snakes = {}    
  
  def add(self, snake: Snake):
    self.snake[snake.get_id()] = snake
    
  def get(self, id):
    return self.snakes.get(id, False)
    
  def get_ids(self):
    return self.snakes.keys()
  
  