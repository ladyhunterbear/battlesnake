from battlesnake2.lib.game.gamestate import GameState
from battlesnake2.lib.strategies.gamestrategy import GameStrategy
from battlesnake2.lib.strategies.solostrategy import SoloStrategy
from battlesnake2.lib.strategies.standardstrategy import StandardStrategy
# from battlesnake2.lib.strategies.duelstrategy import DuelStategy
# from battlesnake2.lib.strategies.arenastrategy import ArenaStategy
# from battlesnake2.lib.strategies.royalestrategy import RoyaleStrategy
from battlesnake2.lib.enums.gametype import GameType


class GameStrategyFactory:
    @staticmethod
    def make(gamestate: GameState) -> GameStrategy:
        strategy = None
        ruleset = gamestate.get_ruleset()
        if ruleset == GameType.SOLO.value:
            strategy = SoloStrategy()
        elif ruleset == GameType.STANDARD.value:
            strategy = StandardStrategy()
        # elif ruleset == GameType.DUEL:
        #     strategy = DuelStrategy()
        # elif ruleset == GameType.ARENA:
        #     strategy = ArenaStrategy()
        # elif ruleset == GameType.ROYALE:
        #     strategy = RoyaleStrategy()
        # else:
        #     strategy = DefaultStrategy()
        
        return strategy
