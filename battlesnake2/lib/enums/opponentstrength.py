from enum import Enum

class OpponentStrength(Enum):
  STRONGER = 1
  EQUAL = 0
  WEAKER = -1
  NULL = -2
  
  
  @classmethod
  def has_value(cls, value):
      return any(value == item.value for item in cls)
