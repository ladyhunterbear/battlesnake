from battlesnake2.lib.strategies.gamestrategy import GameStrategy
from battlesnake2.lib.tactics.gathertactics.gatherertactic import GathererTactic
from battlesnake2.lib.tactics.gathertactics.diettactic import DietTactic
# from battlesnake2.lib.tactics.huntertactics.circulartactic import CircularTactic
# from battlesnake2.lib.tactics.areatactic.edgetactic import EdgeTactic
# from battlesnake2.lib.tactics.areatactics.wanderertactic import WandererTactic
# from battlesnake2.lib.tactics.generaltactics.lookaheadtactic import LookAheadTactic


class SoloStrategy(GameStrategy):
    min_health = 15
    