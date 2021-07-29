from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.coordinates.coordinate import Coordinate

'''
How to live life on the edge
'''
class EdgeTactic(Tactic):
  override_states = [
    GameBoardSquareState.SNAKE_SELF_HEAD.value,
    GameBoardSquareState.SNAKE_SELF_BODY.value,
    GameBoardSquareState.SNAKE_SELF_TAIL.value,
    GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD.value,
    GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD.value,
    GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD.value,
    GameBoardSquareState.SNAKE_ENEMY_BODY.value,
    GameBoardSquareState.SNAKE_ENEMY_TAIL.value,
    GameBoardSquareState.FOOD.value,
    GameBoardSquareState.FOOD_1_STEP.value,
    GameBoardSquareState.FOOD_2_STEPS.value,
    GameBoardSquareState.FOOD_3_STEPS.value,
    GameBoardSquareState.FOOD_4_STEPS.value,
    GameBoardSquareState.HAZARD.value
  ]
  
  def get_corner_coords(self, gameboard: GameBoard) -> list:
    dimensions = gameboard.get_board_dimensions()
    corners = []
    corners.append(Coordinate(0, 0))
    corners.append(Coordinate(dimensions[0] - 1, 0))
    corners.append(Coordinate(0, dimensions[1] - 1))
    corners.append(Coordinate(dimensions[0] - 1, dimensions[1] - 1))
    return corners
  
  def set_corners(self, gameboard: GameBoard) -> GameBoard:
    for corner_coord in self.get_corner_coords(gameboard):
      current_square_state_value = gameboard.get_square(corner_coord).get_state().value
      is_empty = current_square_state_value == GameBoardSquareState.EMPTY.value
      if is_empty or (current_square_state_value > 0 and not current_square_state_value in self.override_states):
        gameboard.get_square(corner_coord).set_state(GameBoardSquareState.EMPTY_CORNER)
    return gameboard
     
  def corner_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):
        current_square_value = gameboard.get_square(coord).get_state().value
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        not_override_state = current_square_value not in self.override_states
        less_than = new_state.value < current_square_value
        if greater_than and not_override_state and less_than:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard
    
  def set_edges_loop(self, gameboard: GameBoard) -> GameBoard:
    for x in range(0,10):
      top_edge_coord = Coordinate(x, 0)
      bottom_edge_coord = Coordinate(x, gameboard.get_board_dimensions()[1] - 1)  
      top_square = gameboard.get_square(top_edge_coord)
      if top_square.get_state() == GameBoardSquareState.EMPTY:
        gameboard.get_square(top_edge_coord).set_state(GameBoardSquareState.EMPTY_EDGE)
      bottom_square = gameboard.get_square(bottom_edge_coord)
      if bottom_square.get_state() == GameBoardSquareState.EMPTY:
        gameboard.get_square(bottom_edge_coord).set_state(GameBoardSquareState.EMPTY_EDGE)   
    for y in range(0,10):
      left_edge_coord = Coordinate(0, y)
      right_edge_coord = Coordinate(gameboard.get_board_dimensions()[0] - 1, y)
      left_square = gameboard.get_square(left_edge_coord)
      if left_square.get_state() == GameBoardSquareState.EMPTY:
        gameboard.get_square(left_edge_coord).set_state(GameBoardSquareState.EMPTY_EDGE)
      right_square = gameboard.get_square(right_edge_coord)
      if right_square.get_state() == GameBoardSquareState.EMPTY:
        gameboard.get_square(right_edge_coord).set_state(GameBoardSquareState.EMPTY_EDGE)
    return gameboard
    
  def edge_loop(self, gameboard: GameBoard, current_state: GameBoardSquareState, new_state: GameBoardSquareState) -> GameBoard:
    for coords in gameboard.filter_type(current_state):
      for coord in gameboard.get_adjacent_coordinates(coords):
        current_square_value = gameboard.get_square(coord).get_state().value
        not_override_square = current_square_value not in self.override_states
        greater_than = current_square_value > GameBoardSquareState.SNAKE_ENEMY_BODY.value
        less_than = new_state.value < current_square_value
        if greater_than and less_than and not_override_square:
          gameboard.get_square(coord).set_state(new_state)
    return gameboard


  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
    gameboard = self.set_edges_loop(gameboard)
    gameboard = self.edge_loop(gameboard, GameBoardSquareState.EMPTY_EDGE, GameBoardSquareState.EMPTY_EDGE_1_STEP)
    gameboard = self.edge_loop(gameboard, GameBoardSquareState.EMPTY_EDGE_1_STEP, GameBoardSquareState.EMPTY_EDGE_2_STEPS)
    gameboard = self.edge_loop(gameboard, GameBoardSquareState.EMPTY_EDGE_2_STEPS, GameBoardSquareState.EMPTY_EDGE_3_STEPS)


    gameboard = self.set_corners(gameboard)
    gameboard = self.corner_loop(gameboard, GameBoardSquareState.EMPTY_CORNER, GameBoardSquareState.EMPTY_CORNER_1_STEP)
    gameboard = self.corner_loop(gameboard, GameBoardSquareState.EMPTY_CORNER_1_STEP, GameBoardSquareState.EMPTY_CORNER_2_STEPS)
    
    return gameboard