from django.test import TestCase
from battlesnake2.game import Game
import json

# Only test cases with 1 obvious outcome. 

class BattleSnake2BoundariesTestCase(TestCase):
  def test_snake_does_not_leave_gameboard_top(self):
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
            {"x": 6, "y": 8}
          ],
          "hazards": [
            {"x": 5, "y": 0}, 
            {"x": 10, "y": 6}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 0, "y": 10}, 
                {"x": 0, "y": 9}, 
                {"x": 0, "y": 8}
              ],
              "latency": "111",
              "head": {"x": 0, "y": 10},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            }
            
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 54,
          "body": [
            {"x": 0, "y": 10}, 
            {"x": 0, "y": 9}, 
            {"x": 0, "y": 8}
          ],
          "latency": "111",
          "head": {"x": 0, "y": 10},
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
    
    
  def test_snake_does_not_leave_gameboard_right(self):
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
            {"x": 6, "y": 8}
          ],
          "hazards": [
            {"x": 5, "y": 0}, 
            {"x": 10, "y": 6}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 10, "y": 10}, 
                {"x": 9, "y": 10}, 
                {"x": 8, "y": 10}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 10},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            }
            
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 54,
          "body": [
            {"x": 10, "y": 10}, 
            {"x": 9, "y": 10}, 
            {"x": 8, "y": 10}
          ],
          "latency": "111",
          "head": {"x": 10, "y": 10},
          "length": 3,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'down', 'shout': 'I should move down'}
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertEqual(expected_response, response)
    
  
  def test_snake_does_not_leave_gameboard_bottom(self):
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
            {"x": 6, "y": 8}
          ],
          "hazards": [
            {"x": 5, "y": 0}, 
            {"x": 10, "y": 6}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 10, "y": 0}, 
                {"x": 10, "y": 1}, 
                {"x": 10, "y": 2}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 0},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            }
            
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 54,
          "body": [
            {"x": 10, "y": 0}, 
            {"x": 10, "y": 1}, 
            {"x": 10, "y": 2}
          ],
          "latency": "111",
          "head": {"x": 10, "y": 0},
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
    
  
  def test_snake_does_not_leave_gameboard_left(self):
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
            {"x": 6, "y": 8}
          ],
          "hazards": [
            {"x": 5, "y": 0}, 
            {"x": 10, "y": 6}
          ],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 0, "y": 0}, 
                {"x": 1, "y": 0}, 
                {"x": 2, "y": 0}
              ],
              "latency": "111",
              "head": {"x": 0, "y": 0},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            }
            
          ]
        },
        "you": {
          "id": "snake-508e96ac-94ad-11ea-bb37",
          "name": "My Snake",
          "health": 54,
          "body": [
            {"x": 0, "y": 0}, 
            {"x": 1, "y": 0}, 
            {"x": 2, "y": 0}
          ],
          "latency": "111",
          "head": {"x": 0, "y": 0},
          "length": 3,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'up', 'shout': 'I should move up'}
     
    req = json.loads(request)
    game2 = Game(req)
    response = game2.get_move()
    self.assertEqual(expected_response, response)