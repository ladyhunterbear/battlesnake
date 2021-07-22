from battlesnake2.lib.strategies import GameStrategy
from battlesnake2.lib.strategems.gatherstrategems.gathererstrategem import GathererStrategem
from battlesnake2.lib.strategies.gatherstrategems.dietstrategem import DietStrategem
from battlesnake2.lib.strategies.hunterstrategems.hunterstrategem import HunterStrategem
from battlesnake2.lib.strategies.hunterstrategems.circularstrategem import CircularStrategem
from battlesnake2.lib.strategies.hunterstrategems.avoidancestrategem import AvoidanceStrategem
from battlesnake2.lib.strategies.hunterstrategems.protectionstrategem import ProtectionStrategem
from battlesnake2.lib.strategies.areastrategems.edgestrategem import EdgeStrategem
from battlesnake2.lib.strategies.areastrategems.edgehunterstrategem import EdgeHunterStrategem
from battlesnake2.lib.strategies.areastrategems.wandererstrategem import WandererStrategem

class ArenaStategy(GameStrategy):
    def process_common(self):
        pass
        
    def process_hunter_strategy(self):
        pass
          
    def process_gather_strategy(self):
        pass
          
    def process_area_strategy(self):
        pass