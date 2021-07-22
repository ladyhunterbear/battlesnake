from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.strategies.arenastrategy import ArenaStrategy
from battlesnake2.lib.strategies.duelstrategy import DuelStrategy
from battlesnake2.lib.strategies.solostrategy import SoloStrategy
from battlesnake2.lib.strategies.royalestrategy import RoyaleStrategy

class GameStrategy:
  strategy: Strategy = None
  
  def __init__(self, mode):
    if mode == GameType.DUEL:
      self.strategy = DuelStategy()
    elif mode == GameType.ROYALE:
      self.strategy = RoyaleStrategy()
    elif mode == GameType.ARENA:
      self.strategy = ArenaStategy()
    elif mode == GameType.SOLO:
      self.strategy = SoloStrategy()  