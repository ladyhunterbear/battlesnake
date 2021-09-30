from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState

'''
If small enough or healthy enough, try looping around in circles.
'''
class CircularTactic(Tactic):
  override_states = [
    GameBoardSquareState.SNAKE_SELF_BODY.value,
    GameBoardSquareState.FOOD.value,
    GameBoardSquareState.HAZARD.value,
    GameBoardSquareState.SNAKE_ENEMY_TAIL.value
  ]
  
  def set_tail_target(self, gameboard: GameBoard) -> GameBoard:
    for tail_coords in gameboard.filter_type(GameBoardSquareState.SNAKE_SELF_TAIL):
      gameboard.get_square(tail_coords).set_state(GameBoardSquareState.SNAKE_SELF_TAIL_TARGET)
    return gameboard
      
  def chaser_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_override_state = current_square_value not in self.override_states
        less_than = current_square_value < new_state.value
        if greater_than and not_override_state and less_than:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
  
  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    # first replace tail with tail_target
    # gameboard = self.set_tail_target(gameboard)
    
    # then update around tail target
    gameboard = self.chaser_loop(gameboard, GameBoardSquareState.SNAKE_SELF_TAIL, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_1_STEP)
    gameboard = self.chaser_loop(gameboard, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_1_STEP, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_2_STEPS)
    gameboard = self.chaser_loop(gameboard, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_2_STEPS, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_3_STEPS)
    gameboard = self.chaser_loop(gameboard, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_3_STEPS, GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_4_STEPS)
    return gameboard