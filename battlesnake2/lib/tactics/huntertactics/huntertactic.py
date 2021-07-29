from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState

'''

'''
class HunterTactic(Tactic):
  my_snake_overrides = [
    GameBoardSquareState.SNAKE_SELF_HEAD.value,
    GameBoardSquareState.SNAKE_SELF_BODY.value,
    GameBoardSquareState.SNAKE_SELF_TAIL.value
  ]
  my_snake_tail_target_override = [
    GameBoardSquareState.SNAKE_SELF_TAIL_TARGET.value,
    GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_1_STEP.value,
    GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_2_STEPS.value,
    GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_3_STEPS.value,
    GameBoardSquareState.SNAKE_SELF_TAIL_TARGET_4_STEPS.value
  ]
  food_hazard_overrides = [
    GameBoardSquareState.FOOD.value,
    GameBoardSquareState.FOOD_1_STEP.value,
    GameBoardSquareState.FOOD_2_STEPS.value,
    GameBoardSquareState.FOOD_3_STEPS.value,
    GameBoardSquareState.HAZARD.value
  ]
  weaker_snake_overrides = [
    GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE.value,
    GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_1_STEP.value,
    GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_2_STEPS.value,
    GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_3_STEPS.value
  ]
  equal_snake_overrides = [
    GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE.value,
    GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP.value,
    GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_2_STEPS.value,
    GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_3_STEPS.value
  ]
  stronger_snake_overrides = [
    GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE.value,
    GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP.value,
    GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS.value,
    GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_3_STEPS.value
  ]
  
  def not_on_edge(self, gameboard: GameBoard, gamestate: GameState) -> bool:
    board_dimensions = gameboard.get_board_dimensions()
    x = gamestate.get_my_snake().get_head().get_x()
    y = gamestate.get_my_snake().get_head().get_y()
    return x > 1 and x < board_dimensions[0] - 2 and y > 1 and y < board_dimensions[1] - 2
  
  def weaker_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_in_override_food = current_square_value not in self.food_hazard_overrides
        not_in_override_my_snake = current_square_value not in self.my_snake_overrides
        not_in_override_weaker_snake = current_square_value not in self.weaker_snake_overrides
        not_override_state = not_in_override_food and not_in_override_my_snake and not_in_override_weaker_snake
        less_than = current_square_value < new_state.value
        if greater_than and not_override_state and less_than:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
    
  def equal_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        less_than = new_state.value < current_square_value
        not_in_override_food = True
        if new_state != GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE:
          not_in_override_food = current_square_value not in self.food_hazard_overrides
        if new_state is not GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE:
          my_snake_overrides = self.my_snake_overrides + self.my_snake_tail_target_override
          not_in_override_my_snake = current_square_value not in my_snake_overrides
        else:
          not_in_override_my_snake = current_square_value not in self.my_snake_overrides
        not_in_override_equal_snake = current_square_value not in self.equal_snake_overrides
        not_override_state = not_in_override_food and not_in_override_my_snake and not_in_override_equal_snake
        if greater_than and less_than and not_override_state:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
  
  def stronger_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):        
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_in_override_food = True
        if new_state != GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE:
          not_in_override_food =  current_square_value not in self.food_hazard_overrides
       
        not_in_override_my_snake = current_square_value not in self.my_snake_overrides
        not_in_override_stronger_snake = current_square_value not in self.stronger_snake_overrides
        not_override_state = not_in_override_my_snake and not_in_override_stronger_snake

        if greater_than and not_override_state:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
  
  def hunter_weaker_snakes(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_1_STEP)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_2_STEPS, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_3_STEPS)
    gameboard = self.weaker_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_3_STEPS, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD_CAN_MOVE_4_STEPS)
    return gameboard
  
  '''
  In some cases we actually want to do the opposite of hunting weaker enemy snakes,
  particularly to prevent getting trapped on the outside edge and running out of 
  space.
  '''  
  def avoid_weaker_snakes(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP)
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_3_STEPS)
    return gameboard
    
  def avoid_equal_snakes(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP)
    # Smaller game boards required less avoidance
    # if gameboard.get_board_dimensions()[0] >= 8 and gameboard.get_board_dimensions()[1] >= 8: 
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    # Biggest game boards allow most avoidance
    # if gameboard.get_board_dimensions()[0] >= 10 and gameboard.get_board_dimensions()[1] >= 10:
    gameboard = self.equal_loop(gameboard, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_2_STEPS, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD_CAN_MOVE_3_STEPS)
    return gameboard
    
  def avoid_stronger_snakes(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE)
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP)
    # Smaller game boards required less avoidance
    #if gameboard.get_board_dimensions()[0] >= 8 and gameboard.get_board_dimensions()[1] >= 8: 
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_1_STEP, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS)
    # Biggest game boards allow most avoidance
    # if gameboard.get_board_dimensions()[0] >= 10 and gameboard.get_board_dimensions()[1] >= 10:
    gameboard = self.stronger_loop(gameboard, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_2_STEPS, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD_CAN_MOVE_3_STEPS)
    return gameboard

  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    if self.not_on_edge(gameboard, gamestate):
      gameboard = self.hunter_weaker_snakes(gameboard, gamestate)
    else:
      gameboard = self.avoid_weaker_snakes(gameboard, gamestate)
    gameboard = self.avoid_equal_snakes(gameboard, gamestate)
    gameboard = self.avoid_stronger_snakes(gameboard, gamestate)
    return gameboard
