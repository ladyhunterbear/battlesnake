from abc import ABC, abstractmethod
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.game.gamestate import GameState


class Tactic(ABC):
    @abstractmethod
    def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        pass
      