from django.test import TestCase
from battlesnake2.game import Game
import json

# Only test cases with 1 obvious outcome. 

class BattleSnake2FoodTestCase(TestCase):
  def test_solo_snake_does_eat_food_when_weak(self):
    request = '''
      {
        "game": {
          "id": "game-00fe20da-94ad-11ea-bb37",
          "ruleset": {
            "name": "standard",
            "version": "v.1.2.3"
          },
          "timeout": 500
        },
        "turn": 14,
        "board": {
          "height": 11,
          "width": 11,
          "food": [
            {"x": 1, "y": 3},
            {"x": 10, "y": 10}
          ],
          "hazards": [
            {"x": 3, "y": 3}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 19,
              "body": [
                {"x": 2, "y": 3}, 
                {"x": 2, "y": 2}, 
                {"x": 3, "y": 2},
                {"x": 4, "y": 2}
              ],
              "latency": "111",
              "head": {"x": 2, "y": 3},
              "length": 4,
              "shout": "why are we shouting??",
              "squad": ""
            }
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 19,
          "body": [
            {"x": 2, "y": 3}, 
            {"x": 2, "y": 2}, 
            {"x": 3, "y": 2},
            {"x": 4, "y": 2}
          ],
          "latency": "111",
          "head": {"x": 2, "y": 3},
          "length": 4,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'left', 'shout': 'I should move left'}
     
    req = json.loads(request)
    response = Game(req).get_move()
    self.assertEqual(expected_response, response)
    
    
  def test_solo_snake_does_not_eat_food_when_healthy(self):
    request = '''
      {
        "game": {
          "id": "game-00fe20da-94ad-11ea-bb37",
          "ruleset": {
            "name": "standard",
            "version": "v.1.2.3"
          },
          "timeout": 500
        },
        "turn": 14,
        "board": {
          "height": 11,
          "width": 11,
          "food": [
            {"x": 1, "y": 3},
            {"x": 10, "y": 10}
          ],
          "hazards": [
            {"x": 3, "y": 3}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 50,
              "body": [
                {"x": 2, "y": 3}, 
                {"x": 2, "y": 2}, 
                {"x": 3, "y": 2},
                {"x": 4, "y": 2}
              ],
              "latency": "111",
              "head": {"x": 2, "y": 3},
              "length": 4,
              "shout": "why are we shouting??",
              "squad": ""
            }
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 50,
          "body": [
            {"x": 2, "y": 3}, 
            {"x": 2, "y": 2}, 
            {"x": 3, "y": 2},
            {"x": 4, "y": 2}
          ],
          "latency": "111",
          "head": {"x": 2, "y": 3},
          "length": 4,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'up', 'shout': 'I should move up'}
     
    req = json.loads(request)
    response = Game(req).get_move()
    self.assertEqual(expected_response, response)
    
    
  def test_solo_snake_moves_closer_to_food_when_hungry(self):
    request = '''
      {
        "game": {
          "id": "game-00fe20da-94ad-11ea-bb37",
          "ruleset": {
            "name": "standard",
            "version": "v.1.2.3"
          },
          "timeout": 500
        },
        "turn": 14,
        "board": {
          "height": 11,
          "width": 11,
          "food": [
            {"x": 2, "y": 4},
            {"x": 10, "y": 10}
          ],
          "hazards": [
            {"x": 3, "y": 3}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 18,
              "body": [
                {"x": 6, "y": 3}, 
                {"x": 6, "y": 4}, 
                {"x": 6, "y": 5},
                {"x": 6, "y": 6}
              ],
              "latency": "111",
              "head": {"x": 6, "y": 3},
              "length": 4,
              "shout": "why are we shouting??",
              "squad": ""
            }
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 18,
          "body": [
            {"x": 6, "y": 3}, 
            {"x": 6, "y": 4}, 
            {"x": 6, "y": 5},
            {"x": 6, "y": 6}
          ],
          "latency": "111",
          "head": {"x": 6, "y": 3},
          "length": 4,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'left', 'shout': 'I should move left'}
     
    req = json.loads(request)
    response = Game(req).get_move()
    self.assertEqual(expected_response, response)
    
    