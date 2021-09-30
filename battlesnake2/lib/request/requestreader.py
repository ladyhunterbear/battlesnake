from battlesnake2.lib.enums.gametype import GameType
from battlesnake2.lib.snakes.snakescollection import SnakesCollection
from battlesnake2.lib.snakes.snake import Snake
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.food.foodcollection import FoodCollection
from battlesnake2.lib.food.food import Food
from battlesnake2.lib.hazard.hazardcollection import HazardCollection
from battlesnake2.lib.hazard.hazard import Hazard
from battlesnake2.lib.coordinates.coordinate import Coordinate

'''
Read the BattleSnake json request and produce a GameState
Separate reading from JSON and converting to objects from doing anything with that resulting object.
'''
class RequestReader:
  request: object
  
  def __init__(self, request):
    self.request = request
  
  '''
  Returns an GameBoard based on request
  '''
  def gameboard(self) -> GameBoard:
    gameboard = GameBoard()
    gameboard.set_board_dimensions(self.request['board']['height'], self.request['board']['width'])
    gameboard.initialize_gameboard_squares()
    return gameboard
  
  '''
  Get the name of the game ruleset
  '''
  def ruleset(self) -> str:
    return self.request['game']['ruleset']['name']
  
  '''
  Returns a Snake object from 'you' property of request.
  '''
  def my_snake(self) -> Snake:
    return Snake(self.request['you'])
  
  '''
  Returns SnakeCollection of 0 or more Snake objects based on opponents found in request.
  '''
  def opponents(self):
    snakes_collection = SnakesCollection()
    request_snakes = self.request['board']['snakes']
    if (len(request_snakes) > 1):
      for request_snake in request_snakes:
        snake = Snake(request_snake)
        if snake.is_alive() and snake.get_id() != self.my_snake().get_id():
          snakes_collection.set(snake)
    return snakes_collection
  
  '''
  Returns a FoodCollection of 0 or more Food objects based on request.
  '''
  def food(self):
    food_collection = FoodCollection()
    foods = self.request['board']['food']
    for food in foods:
      food_collection.set(Food(Coordinate(food['x'], food['y'])))
    return food_collection

  '''
  Returns a HazardCollection of 0 or more Hazard objects based on request.
  '''
  def hazards(self):
    hazard_collection = HazardCollection()
    hazards = self.request['board']['hazards']
    for hazard in hazards:
      hazard_collection.set(Hazard(Coordinate(hazard['x'], hazard['y']))) 
    return hazard_collection
