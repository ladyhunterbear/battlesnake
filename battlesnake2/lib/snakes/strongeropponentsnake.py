from battlesnake2.snake import Snake

class StrongerOpponentSnake(Snake):
  
  '''
  Add opponent snakes to the gameboard
  '''
  def add_to_gameboard(self):
      if self.snakes.is_empty():
          return None
      
      for snake in self.snakes:
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
          
     