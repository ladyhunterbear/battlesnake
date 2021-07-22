from enum import Enum

class LookAheadSquareState(Enum):
    MOVE_0 = 900
    MOVE_1 = 901
    MOVE_2 = 902
    MOVE_3 = 903
    MOVE_4 = 904
    MOVE_5 = 905
    MOVE_6 = 906
    MOVE_7 = 907
    MOVE_8 = 908
    MOVE_9 = 909
    MOVE_10 = 910
    
    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)
