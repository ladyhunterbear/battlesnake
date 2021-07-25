from battlesnake2.lib.gameboard.gameboard import GameBoard
from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.strategies.gamestrategy import GameStrategy
from battlesnake2.lib.tactics.huntertactics.huntertactic import HunterTactic
from battlesnake2.lib.tactics.huntertactics.circulartactic import CircularTactic
from battlesnake2.lib.tactics.areatactics.edgetactic import EdgeTactic

class StandardStrategy(GameStrategy):
    min_health = 20
    
    def predator_close(self, gameboard: GameBoard, gamestate: GameState) -> bool:
        my_snake = gamestate.get_my_snake()
        opponents = gamestate.get_opponents()
        for id in gamestate.get_opponents().get_ids():            
            opponent = opponents.get(id)
            opponent_longer =  opponent.get_length() > my_snake.get_length()
            opponent_equal =  opponent.get_length() == my_snake.get_length()
            distance_to_opponent = gameboard.distance(opponent.get_head(), my_snake.get_head())
            if (opponent_longer or opponent_equal) and distance_to_opponent <= 4:
                return True
        return False
    
    def _before(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        gameboard = super(StandardStrategy, self)._before(gameboard, gamestate)
        # Prefer avoiding edges and corners
        edge_tactic = EdgeTactic()
        gameboard = edge_tactic.apply(gameboard, gamestate)
        # Defensive maneuvers if enemy close!
        if self.predator_close(gameboard, gamestate):
            circular_tactic = CircularTactic()
            gameboard = circular_tactic.apply(gameboard, gamestate)
        return gameboard
    
    def _tactics(self, gameboard: GameBoard, gamestate: GameState) -> GameBoard:
        hunter_tactic = HunterTactic()
        gameboard = hunter_tactic.apply(gameboard, gamestate)
        return gameboard
        
    