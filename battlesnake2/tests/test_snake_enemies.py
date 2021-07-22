from django.test import TestCase
from battlesnake2.game import Game
import json

# Only test cases with 1 obvious outcome. 

class BattleSnake2StandardStrategyTestCase(TestCase):
  def test_snake_avoids_stronger_opponents(self):
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
            {"x": 2, "y": 3},
            {"x": 10, "y": 1}
          ],
          "hazards": [
            {"x": 5, "y": 0}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 8, "y": 6}, 
                {"x": 8, "y": 7}, 
                {"x": 8, "y": 8}
              ],
              "latency": "111",
              "head": {"x": 8, "y": 6},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb38",
              "name": "Enemy Snake",
              "health": 100,
              "body": [
                {"x": 10, "y": 6}, 
                {"x": 10, "y": 7}, 
                {"x": 10, "y": 8}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 6},
              "length": 3,
              "shout": "hungry hungry hippo",
              "squad": ""
            }
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 54,
          "body": [
            {"x": 8, "y": 6}, 
            {"x": 8, "y": 7}, 
            {"x": 8, "y": 8}
          ],
          "latency": "111",
          "head": {"x": 8, "y": 6},
          "length": 3,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'left', 'shout': 'I should move left'}
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertEqual(expected_response, response)
    
    
  def test_snake_attacks_weaker_opponents(self):
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
            {"x": 2, "y": 3},
            {"x": 10, "y": 1}
          ],
          "hazards": [
            {"x": 5, "y": 0}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 8, "y": 6}, 
                {"x": 8, "y": 7}, 
                {"x": 8, "y": 8}
              ],
              "latency": "111",
              "head": {"x": 8, "y": 6},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb38",
              "name": "Enemy Snake",
              "health": 20,
              "body": [
                {"x": 10, "y": 8}, 
                {"x": 10, "y": 9}, 
                {"x": 10, "y": 10}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 8},
              "length": 3,
              "shout": "hungry hungry hippo",
              "squad": ""
            }
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 54,
          "body": [
            {"x": 8, "y": 6}, 
            {"x": 8, "y": 7}, 
            {"x": 8, "y": 8}
          ],
          "latency": "111",
          "head": {"x": 8, "y": 6},
          "length": 3,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'right', 'shout': 'I should move right'}
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertEqual(expected_response, response)
    
    
  def test_snake_ingores_equal_opponents(self):
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
            {"x": 2, "y": 3},
            {"x": 10, "y": 1}
          ],
          "hazards": [
            {"x": 5, "y": 0}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 50,
              "body": [
                {"x": 8, "y": 6}, 
                {"x": 8, "y": 7}, 
                {"x": 8, "y": 8}
              ],
              "latency": "111",
              "head": {"x": 8, "y": 6},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb38",
              "name": "Enemy Snake",
              "health": 50,
              "body": [
                {"x": 10, "y": 6}, 
                {"x": 10, "y": 7}, 
                {"x": 10, "y": 8}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 6},
              "length": 3,
              "shout": "hungry hungry hippo",
              "squad": ""
            }
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 50,
          "body": [
            {"x": 8, "y": 6}, 
            {"x": 8, "y": 7}, 
            {"x": 8, "y": 8}
          ],
          "latency": "111",
          "head": {"x": 8, "y": 6},
          "length": 3,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'left', 'shout': 'I should move left'}
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertEqual(expected_response, response)