from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState

'''

'''
class HunterTactic(Tactic):
  override_states = [
    GameBoardSquareState.SNAKE_SELF_BODY.value,
    GameBoardSquareState.SNAKE_SELF_TAIL.value,
    GameBoardSquareState.FOOD.value,
    GameBoardSquareState.HAZARD.value
  ]
  def weaker_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_override_state = current_square_value not in self.override_states
        less_than = current_square_value < new_state.value
        if greater_than and not_override_state and less_than:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
    
  def equal_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_override_state = current_square_value not in self.override_states
        if greater_than and not_override_state:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
  
  def stronger_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_override_state = current_square_value not in self.override_states
        if greater_than and not_override_state:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
  
  
  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    # WEAKER ENEMY
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_1_STEP)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_2_STEP)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_2_STEP, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_3_STEP)
     
    #EQUAL ENEMY
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP)
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    
    # STRONGER ENEMY
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP)
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    
    return gameboard
