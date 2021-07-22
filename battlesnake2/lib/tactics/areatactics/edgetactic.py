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
    GameBoardSquareState.SNAKE_SELF_TAIL.value,
    GameBoardSquareState.FOOD.value,
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
    
  def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:    
    gameboard = self.set_corners(gameboard)
    gameboard = self.corner_loop(gameboard, GameBoardSquareState.EMPTY_CORNER, GameBoardSquareState.EMPTY_CORNER_1_STEP)
    gameboard = self.corner_loop(gameboard, GameBoardSquareState.EMPTY_CORNER_1_STEP, GameBoardSquareState.EMPTY_CORNER_2_STEPS)
    return gameboard