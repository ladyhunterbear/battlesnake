from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.gameboard.gameboardsquarecollection import GameBoardSquareCollection

'''

'''
class GathererTactic(Tactic):
  def loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        less_than = new_state.value > current_square_value
        if greater_than and less_than:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
    
  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:   
    gameboard = self.loop(gameboard, GameBoardSquareState.FOOD, GameBoardSquareState.FOOD_1_STEP)
    gameboard = self.loop(gameboard, GameBoardSquareState.FOOD_1_STEP, GameBoardSquareState.FOOD_2_STEPS)
    gameboard = self.loop(gameboard, GameBoardSquareState.FOOD_2_STEPS, GameBoardSquareState.FOOD_3_STEPS)
    gameboard = self.loop(gameboard, GameBoardSquareState.FOOD_3_STEPS, GameBoardSquareState.FOOD_4_STEPS)

    return gameboard
