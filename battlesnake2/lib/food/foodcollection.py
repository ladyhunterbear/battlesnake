
from battlesnake2.lib.gameboard.gameboardsquarecollection import GameBoardSquareCollection
from battlesnake2.lib.food.food import Food


class FoodCollection(GameBoardSquareCollection):
  def __init__(self):
    super(FoodCollection, self).__init__()
    