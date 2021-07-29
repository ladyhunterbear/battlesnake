from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.tactics.gathertactics.gatherertactic import GathererTactic
from battlesnake2.lib.tactics.gathertactics.diettactic import DietTactic
from battlesnake2.lib.tactics.lookaheadtactics.lookaheadtactic import LookAheadTactic
from battlesnake2.lib.game.gamestate import GameState

class GameStrategy: 
    min_health = 30
        
    def _my_snake_health_low(self, gamestate: GameState) -> bool:
        return self.min_health > gamestate.get_my_snake().get_health()
            
    def _equal_or_longer_opponent(self, gamestate: GameState) -> bool:
        my_snake_length = gamestate.get_my_snake().get_length()
        opponents = gamestate.get_opponents()
        for opponent_id in opponents.get_ids():
            if opponents.get(opponent_id).get_length() >= my_snake_length - 2:
                return True
        return False
        
    '''
    A collection of tactics that should be applied all the time as a base
    regardless of game type.
    '''
    def _before(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        if (self._my_snake_health_low(gamestate) or self._equal_or_longer_opponent(gamestate)):
            gather_tactic = GathererTactic()
            gameboard = gather_tactic.apply(gameboard, gamestate)
        else:
            diet_tactic = DietTactic()
            gameboard = diet_tactic.apply(gameboard, gamestate) 
        # lookAheadTactic = LookAheadTactic()
        # gameboard = lookAheadTactic.apply(gameboard)
        return gameboard
            
    def _tactics(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        return gameboard
        
    def _after(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        lookahead_tactic = LookAheadTactic()
        gameboard = lookahead_tactic.apply(gameboard, gamestate)
        return gameboard

    def process(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        gameboard = self._before(gameboard, gamestate)
        gameboard = self._tactics(gameboard, gamestate)
        gameboard = self._after(gameboard, gamestate)
        return gameboard
    