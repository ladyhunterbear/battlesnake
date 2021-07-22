from enum import Enum

class GameType(Enum):  
  DUEL = 'duel'
  ROYALE = 'royale'
  ARENA = 'arena'
  SOLO = 'solo'
  STANDARD = 'standard'
  CHALLENGE_SOLO_SURVIVAL = 'challenge_solo_survival'
  CHALLENGE_LONG_SNAKE = 'challenge_long_snake'
  
  # ...
  
  @classmethod
  def has_value(cls, value):
      return any(value == item.value for item in cls)
  