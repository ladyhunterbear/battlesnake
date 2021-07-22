from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.coordinates.coordinate import Coordinate

class GameBoardSquare:
    state = GameBoardSquareState.NULL
    coordinates = None
    
    def set_state(self, state: GameBoardSquareState) -> GameBoardSquareState:
        self.state = state

        
    def get_state(self) -> GameBoardSquareState:
        return self.state

        
    def get_state_value(self) -> int:
        return self.state.value


    def set_coordinates(self, coordinates: Coordinate) -> Coordinate:
        self.coordinates = coordinates


    def get_coordinates(self) -> Coordinate:
        return self.coordinates


    def __init__(self, coordinates: Coordinate, state: GameBoardSquareState):
        self.set_coordinates(coordinates)
        self.set_state(state)