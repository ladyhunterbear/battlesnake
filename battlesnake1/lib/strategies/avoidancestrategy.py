from battlesnake1.lib.strategies.strategyinterface import StrategyInterface
from battlesnake1.gameboard import GameBoard
from battlesnake1.gameboardsquare import GameBoardSquare
from battlesnake1.lib.enums.gameboardsquarestate import GameBoardSquareState

'''

'''
class AvoidanceStrategy(StrategyInterface):
  gameboard = None
  
  def should_update_square_state(self, possible_square: GameBoardSquare, test_state: GameBoardSquareState) -> bool:
    return possible_square.get_state_value() > 0 and possible_square.get_state_value() > test_state.value
      
  
  def evaluate_surrouding_square_states(self, state, new_state):
    for square_key in self.gameboard.squares:
      square = self.gameboard.squares[square_key]
      if square.get_state() == state:
        possible_direction_coords = self.gameboard.get_surrounding_squares(square.get_coordinates())
        for direction in possible_direction_coords:
          possible_square = self.gameboard.get_square(possible_direction_coords[direction])
          if self.should_update_square_state(possible_square, new_state):
            possible_square.set_state(new_state)
                    
      
  def process(self, gameboard: GameBoard) -> GameBoard:
    self.gameboard = gameboard
    
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE)
    
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP)
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE)

    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP)
    
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP)
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_ENEMY_BODY, GameBoardSquareState.SNAKE_ENEMY_BODY_1_STEP)
    
    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_ENEMY_BODY_1_STEP, GameBoardSquareState.SNAKE_ENEMY_BODY_2_STEPS)

    self.evaluate_surrouding_square_states(GameBoardSquareState.SNAKE_SELF_BODY, GameBoardSquareState.SNAKE_SELF_BODY_1_STEP)
    
    return self.gameboard
