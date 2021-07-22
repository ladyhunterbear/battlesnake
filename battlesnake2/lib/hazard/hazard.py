from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.coordinates.coordinate import Coordinate

class Hazard(GameBoardSquare):
  def __init__(self, coordinates: Coordinate, state: GameBoardSquare = GameBoardSquareState.HAZARD):
    super(Hazard, self).__init__(coordinates, state)
