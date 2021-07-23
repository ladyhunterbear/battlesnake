from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.enums.lookaheadsquarestate import LookAheadSquareState
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.coordinates.coordinate import Coordinate
import copy

class LookAheadTactic(Tactic):
    bad_lookahead = 5
    poor_lookahead = 10
    questionable_lookahead = 15
    
    override_values = [
        GameBoardSquareState.FOOD.value,
        GameBoardSquareState.HAZARD.value,
        GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD.value,
        GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD.value,
        GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD.value,
        GameBoardSquareState.SNAKE_ENEMY_BODY.value,
        GameBoardSquareState.SNAKE_ENEMY_TAIL.value,
        GameBoardSquareState.SNAKE_SELF_HEAD.value,
        GameBoardSquareState.SNAKE_SELF_BODY.value,
        GameBoardSquareState.SNAKE_SELF_TAIL.value
    ]
    
    lookahead_values = [
        LookAheadSquareState.MOVE_0.value,
        LookAheadSquareState.MOVE_1.value,
        LookAheadSquareState.MOVE_2.value,
        LookAheadSquareState.MOVE_3.value,
        LookAheadSquareState.MOVE_4.value,
        LookAheadSquareState.MOVE_5.value,
        LookAheadSquareState.MOVE_6.value,
        LookAheadSquareState.MOVE_7.value,
        LookAheadSquareState.MOVE_8.value,
        LookAheadSquareState.MOVE_9.value,
        LookAheadSquareState.MOVE_10.value
    ]
    
    lookahead_states = [
        LookAheadSquareState.MOVE_0,
        LookAheadSquareState.MOVE_1,
        LookAheadSquareState.MOVE_2,
        LookAheadSquareState.MOVE_3,
        LookAheadSquareState.MOVE_4,
        LookAheadSquareState.MOVE_5,
        LookAheadSquareState.MOVE_6,
        LookAheadSquareState.MOVE_7,
        LookAheadSquareState.MOVE_8,
        LookAheadSquareState.MOVE_9,
        LookAheadSquareState.MOVE_10
    ]
    
    def tally_lookahead(self, gameboard: GameBoard):
        tally = 0
        for state in self.lookahead_states:
            tally = tally + len(gameboard.filter_type(state))
        return tally
        
    def loop(self, gameboard: GameBoard, current_state: LookAheadSquareState, new_state: LookAheadSquareState) -> GameBoard:
        for coords in gameboard.filter_type(current_state):
          for coord in gameboard.get_adjacent_coordinates(coords):
            not_in_override_states = gameboard.get_square(coord).get_state().value not in self.override_values
            not_in_lookahead_states = gameboard.get_square(coord).get_state().value not in self.lookahead_values
            if not_in_lookahead_states and not_in_override_states:
                gameboard.get_square(coord).set_state(new_state)
        return gameboard
      
    def apply(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        # get possible directions from head - these are the important ones
        possible_directions = gameboard.get_possible_directions(gamestate.get_my_snake().get_head())
        
        for direction in possible_directions:
            gb = copy.deepcopy(gameboard)
            
            gb.get_square(possible_directions[direction]).set_state(LookAheadSquareState.MOVE_0)
            gb = self.loop(gb, LookAheadSquareState.MOVE_0, LookAheadSquareState.MOVE_1)
            gb = self.loop(gb, LookAheadSquareState.MOVE_1, LookAheadSquareState.MOVE_2)
            gb = self.loop(gb, LookAheadSquareState.MOVE_2, LookAheadSquareState.MOVE_3)
            gb = self.loop(gb, LookAheadSquareState.MOVE_3, LookAheadSquareState.MOVE_4)
            gb = self.loop(gb, LookAheadSquareState.MOVE_4, LookAheadSquareState.MOVE_5)
            gb = self.loop(gb, LookAheadSquareState.MOVE_5, LookAheadSquareState.MOVE_6)
            gb = self.loop(gb, LookAheadSquareState.MOVE_6, LookAheadSquareState.MOVE_7)
            gb = self.loop(gb, LookAheadSquareState.MOVE_7, LookAheadSquareState.MOVE_8)
            # gb = self.loop(gb, LookAheadSquareState.MOVE_8, LookAheadSquareState.MOVE_9)
            # gb = self.loop(gb, LookAheadSquareState.MOVE_9, LookAheadSquareState.MOVE_10)
            
            tally = self.tally_lookahead(gb)
            if tally <= self.bad_lookahead:
                gameboard.get_square(possible_directions[direction]).set_state(GameBoardSquareState.BAD_LOOKAHEAD)
            elif tally > self.bad_lookahead and tally <= self.poor_lookahead:
                gameboard.get_square(possible_directions[direction]).set_state(GameBoardSquareState.POOR_LOOKAHEAD)
            elif tally > self.poor_lookahead and tally <= self.questionable_lookahead:
                gameboard.get_square(possible_directions[direction]).set_state(GameBoardSquareState.QUESTIONABLE_LOOKAHEAD)
            # print("----- LOOKAHEAD ------")    
            # print(gb.get_board_matrix())
            # print("----- Tally: " + str(tally) + " ------")
        return gameboard