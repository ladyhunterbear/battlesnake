from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.snakes.snakescollection import SnakesCollection
from battlesnake2.lib.snakes.snake import Snake
from battlesnake2.lib.hazard.hazardcollection import HazardCollection
from battlesnake2.lib.food.foodcollection import FoodCollection
from battlesnake2.lib.enums.gametype import GameType
from battlesnake2.lib.request.requestreader import RequestReader


'''
A class representing the immutable GameState.
Similar to other frameworks like React or Vue.
'''
class GameState:
  def __init__(self):
    self.gameboard: GameBoard = GameBoard()
    self.ruleset: GameType = GameType.STANDARD
    self.opponents: SnakesCollection = SnakesCollection()
    self.my_snake: Snake = None
    self.food: FoodCollection = FoodCollection()
    self.hazards: HazardCollection = HazardCollection()
    
  def set_gameboard(self, gameboard: GameBoard): 
    self.gameboard = gameboard
  
  def get_gameboard(self) -> GameBoard:
    return self.gameboard
    
  def set_opponents(self, opponents: SnakesCollection):
    self.opponents = opponents
    
  def get_opponents(self) -> SnakesCollection:
    return self.opponents

  def set_my_snake(self, my_snake: Snake):
    self.my_snake = my_snake
      
  def get_my_snake(self) -> Snake:
    return self.my_snake
    
  def set_food(self, food: FoodCollection):
    self.food = food

  def get_food(self) -> FoodCollection:
    return self.food
      
  def set_hazards(self, hazards: HazardCollection):
    self.hazards = hazards
    
  def get_hazards(self) -> HazardCollection:
    return self.hazards

  def set_ruleset(self, ruleset: GameType):  
    self.ruleset = ruleset
   
  def get_ruleset(self) -> GameType:
    return self.ruleset