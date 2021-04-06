from battlesnake1.lib.strategies.strategyinterface import StrategyInterface
from battlesnake1.gameboard import GameBoard
from battlesnake1.gameboardsquare import GameBoardSquare
from battlesnake1.lib.enums.gameboardsquarestate import GameBoardSquareState

'''
Based on games where I was killed by an attacking snake on the outside, 
as a result of getting penned in, is it better to stay away from the edges?
'''
class ProtectionStrategy(StrategyInterface):
  gameboard = None
  
  def should_update_edge_square_state(self, possible_square: GameBoardSquare, test_state: GameBoardSquareState) -> bool:
    return possible_square.get_state_value() == GameBoardSquareState.EMPTY
 
  def should_update_square_state(self, possible_square: GameBoardSquare, test_state: GameBoardSquareState) -> bool:
    return possible_square.get_state_value() > test_state.value
  
  def evaluate_gameboard_for_edges(self):
    for square_key in self.gameboard.squares:
      square = self.gameboard.squares[square_key]
      possible_direction_coords = self.gameboard.get_surrounding_squares(square.get_coordinates())
      if len(possible_direction_coords) == 3 and square.get_state_value() > 0:
        square.set_state(GameBoardSquareState.EMPTY_EDGE)
      elif len(possible_direction_coords) == 2 and square.get_state_value() > 0:
        square.set_state(GameBoardSquareState.EMPTY_CORNER)

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
    
    self.evaluate_gameboard_for_edges()
    self.evaluate_surrouding_square_states(GameBoardSquareState.EMPTY_EDGE, GameBoardSquareState.EMPTY_EDGE_1_STEP)
    self.evaluate_surrouding_square_states(GameBoardSquareState.EMPTY_CORNER, GameBoardSquareState.EMPTY_CORNER_1_STEP)
    self.evaluate_surrouding_square_states(GameBoardSquareState.EMPTY_CORNER_1_STEP, GameBoardSquareState.EMPTY_CORNER_2_STEPS)
    self.evaluate_surrouding_square_states(GameBoardSquareState.EMPTY_CORNER_2_STEPS, GameBoardSquareState.EMPTY_CORNER_3_STEPS)
    
    return self.gameboard
    
    # add check for hazards
    # add check for edges
    # then what, anything else?