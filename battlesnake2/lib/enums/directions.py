from enum import Enum

class Direction(Enum):
  UP = 'up'
  RIGHT = 'right'
  DOWN = 'down'
  LEFT = 'left'
  
  @classmethod
  def has_value(cls, value):
      return any(value == item.value for item in cls)
  