from battlesnake2.lib.strategies import GameStrategy
from battlesnake2.lib.tatics.gathertactics.gathertactic import GathererTactic
from battlesnake2.lib.tatics.gathertactics.gathertactic import DietTactic
from battlesnake2.lib.tactics.huntertactics.huntertactic import HunterTactic
from battlesnake2.lib.tactics.huntertactics.circulartactic import CircularTactic
from battlesnake2.lib.tactics.huntertactics.avoidancetactic import AvoidanceTactic
from battlesnake2.lib.tactics.huntertactics.protectiontactic import ProtectionTactic
from battlesnake2.lib.tactics.areatactics.edgetactic import EdgeTactic
from battlesnake2.lib.tactics.areatactics.edgehuntertactic import EdgeHunterTactic
from battlesnake2.lib.tactics.areatactics.wanderertactic import WandererTactic

class DuelStategy(GameStrategy):
    min_health < 20
    
    def __tactics(gamevision: GameBoard, gamestate: GameState) -> GameBoard:
        # Move this into PlayerStrategy with a .get()
        player_strategies = PlayerStrategy()
        for player_strategy in player_strategies.get():
            gamevision = player_strategy.process(gamevision, gamestate)
                
        # To eat or not to eat...
        if gamestate.get_my_snake().get_health() < min_health:
            gather_tactic = GathererTactic()
            gamevision = gather_tactic.process(gamevision, gamestate)
        else:
            diet_tactic = DietTactic()
            gamevision = diet_tactic.process(gamevision, gamestate)
        return gamevision
    
    def process_common(self):
        wanderer_strategy = WandererStrategy()
        self.gameboard = wanderer_strategy.process(self.gameboard)
        #Avoidance Strategy
        avoidance_strategy = AvoidanceStrategy()
        self.gameboard = avoidance_strategy.process(self.gameboard)
      
    def process_hunter_strategy(self):
        # Protection Strategy
        # An edge avoidance strategy that should only apply away from edges
        x = self.my_snake.get_head().get_x()
        y = self.my_snake.get_head().get_y()
        if (x >= 1 and x <= self.gameboard.width - 2) and (y >= 1 and y <= self.gameboard.height - 2):
            protection_strategy = ProtectionStrategy()
            self.gameboard = protection_strategy.process(self.gameboard)
        else:
            edge_strategy = EdgeStrategy()
            self.gameboard = edge_strategy.process(self.gameboard)
            
            
    def process_gather_strategy(self):
        # Gatherer Strategy
        if (self.my_snake.get_health() < 25) or (self.my_snake.get_length() < self.snakes.get_longest_length()):
            gatherer_strategy = GathererStrategy()
            self.gameboard = gatherer_strategy.process(self.gameboard)
        else:
            diet_strategy = DietStrategy()
            self.gameboard = diet_strategy.process(self.gameboard)


    def process_area_strategy(self):
        # Hunter Strategy
        if (x >= 1 and x <= self.gameboard.width - 2) and (y >= 1 and y <= self.gameboard.height - 2):
            hunter_strategy = HunterStrategy()
            self.gameboard = hunter_strategy.process(self.gameboard)
        else:
            edge_hunter_strategy = EdgeHunterStrategy()
            self.gameboard = edge_hunter_strategy.process(self.gameboard)
        

        
        