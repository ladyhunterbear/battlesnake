
from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.game.gamestate import GameState

class DietTactic(Tactic):
  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    squares = gameboard.get_squares().get_all()
    for square in squares:
      if squares[square].get_state() == GameBoardSquareState.FOOD:
        squares[square].set_state(GameBoardSquareState.AVOID_FOOD)
        gameboard.set_square(squares[square])
    return gameboard