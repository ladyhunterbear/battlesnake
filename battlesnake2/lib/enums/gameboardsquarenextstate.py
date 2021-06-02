from enum import Enum

class GameBoardSquareNextState(Enum):
    ANYONE_CAN_MOVE = 1
    I_CAN_MOVE = 10
    WEAKER_ENEMY_CAN_MOVE = 100
    SMALLER_ENEMY_CAN_MOVE = 100
    EQUAL_ENEMY_CAN_MOVE = 0
    STRONGER_EQUAL_ENEMY_CAN_MOVE = 0
    BIGGER_ENEMY_CAN_MOVE = 0
    NO_ONE_CAN_MOVE = 0
    NULL = 0
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)
    
