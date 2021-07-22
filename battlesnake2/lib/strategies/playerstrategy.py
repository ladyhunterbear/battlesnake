from battlesnake2.lib.strategies.gamestrategy import GameStrategy
from battlesnake2.lib.tactics.tactic import Tactic
from battlesnake2.lib.tactics.playertactics.ddtplayertactic import DdtPlayerTactic

class PlayerStrategy(GameStrategy):
    player_tactics: {
        'DDT':  DdtPlayerTactic(),
    }
    
    def get(self, player_names: list) -> list:
        tactics = []
        for player_name in player_names:
            if player_name in self.player_tactics:
                tactics.append(self.player_tactics[player_name])
        return tactics
    