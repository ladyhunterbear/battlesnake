from battlesnake1.lib.strategies.strategyinterface import StrategyInterface
from battlesnake1.gameboard import GameBoard

'''
Look for opportunity to cut off other snakes in pursuit...
where enemy head is beside first body part after head...

'''
class CircularStrategy(StrategyInterface):
  def process(self, gameboard: GameBoard) -> GameBoard:
    
    pass