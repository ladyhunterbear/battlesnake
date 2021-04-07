from battlesnake1.lib.strategies.strategyinterface import StrategyInterface
from battlesnake1.gameboard import GameBoard
from battlesnake1.lib.enums.gameboardsquarestate import GameBoardSquareState

class DietStrategy(StrategyInterface):
  def process(self, gameboard: GameBoard) -> GameBoard:
    self.gameboard = gameboard
    for square in self.gameboard.squares:
      if self.gameboard.squares[square].get_state() == GameBoardSquareState.FOOD:
        self.gameboard.squares[square].set_state(GameBoardSquareState.AVOID_FOOD)
    return self.gameboard