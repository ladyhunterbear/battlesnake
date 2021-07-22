from  battlesnake2.snake import Snake

class MySnake(Snake):
  '''
  Add my snake to the gameboard
  '''
  def add_to_gameboard(self):
      for body_coords in self.my_snake.body:
          coord = Coordinate(self.my_snake.body[body_coords].get_x(), self.my_snake.body[body_coords].get_y())
          square = self.gameboard.get_square(coord)
          square.set_state(GameBoardSquareState.SNAKE_SELF_BODY)
      head_coord = Coordinate(self.my_snake.get_head().get_x(), self.my_snake.get_head().get_y())
      head_square = self.gameboard.get_square(head_coord)
      head_square.set_state(GameBoardSquareState.SNAKE_SELF_HEAD)
  
  