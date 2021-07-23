from django.test import TestCase
from battlesnake2.game import Game
import json

# Only test cases with 1 obvious outcome. 

class BattleSnake2LookAheadTestCase(TestCase):
  def test_snake_does_not_loop_on_self(self):
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
                {"x": 5, "y": 5}, 
                {"x": 5, "y": 4}, 
                {"x": 4, "y": 4},
                {"x": 3, "y": 4},
                {"x": 2, "y": 4},
                {"x": 1, "y": 4},
                {"x": 0, "y": 4},
                {"x": 0, "y": 5},
                {"x": 0, "y": 6},
                {"x": 1, "y": 6},
                {"x": 2, "y": 6},
                {"x": 3, "y": 6},
                {"x": 4, "y": 6},
                {"x": 5, "y": 6}
              ],
              "latency": "111",
              "head": {"x": 5, "y": 5},
              "length": 14,
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
            {"x": 5, "y": 5}, 
            {"x": 5, "y": 4}, 
            {"x": 4, "y": 4},
            {"x": 3, "y": 4},
            {"x": 2, "y": 4},
            {"x": 1, "y": 4},
            {"x": 0, "y": 4},
            {"x": 0, "y": 5},
            {"x": 0, "y": 6},
            {"x": 1, "y": 6},
            {"x": 2, "y": 6},
            {"x": 3, "y": 6},
            {"x": 4, "y": 6},
            {"x": 5, "y": 6}
          ],
          "latency": "111",
          "head": {"x": 5, "y": 5},
          "length": 14,
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
    
  
  def test_snake_does_not_follow_dead_ends(self):
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
                {"x": 0, "y": 3}, 
                {"x": 0, "y": 2}, 
                {"x": 0, "y": 1},
                {"x": 1, "y": 1},
                {"x": 2, "y": 1},
                {"x": 3, "y": 1},
                {"x": 4, "y": 1},
                {"x": 5, "y": 1},
                {"x": 6, "y": 1},
                {"x": 7, "y": 1},
                {"x": 8, "y": 1},
                {"x": 9, "y": 1},
                {"x": 10, "y": 1}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 1},
              "length": 13,
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
            {"x": 0, "y": 3}, 
            {"x": 0, "y": 2}, 
            {"x": 0, "y": 1},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 3, "y": 1},
            {"x": 4, "y": 1},
            {"x": 5, "y": 1},
            {"x": 6, "y": 1},
            {"x": 7, "y": 1},
            {"x": 8, "y": 1},
            {"x": 9, "y": 1},
            {"x": 10, "y": 1}
          ],
          "latency": "111",
          "head": {"x": 10, "y": 1},
          "length": 13,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'up', 'shout': 'I should move up'}
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertEqual(expected_response, response) 
    
    
  def test_snake_should_pick_lesser_bad_choice(self):
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
          "hazards": [],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb39",
              "name": "Enemy Snake",
              "health": 54,
              "body": [
                {"x": 7, "y": 9}, 
                {"x": 7, "y": 8}, 
                {"x": 6, "y": 8},
                {"x": 6, "y": 7},
                {"x": 5, "y": 7},
                {"x": 5, "y": 6},
                {"x": 5, "y": 5},
                {"x": 5, "y": 4},
                {"x": 5, "y": 3},
                {"x": 5, "y": 2},
                {"x": 6, "y": 2},
                {"x": 7, "y": 2},
                {"x": 8, "y": 2},
                {"x": 9, "y": 2},
                {"x": 10, "y": 2}
              ],
              "latency": "111",
              "head": {"x": 7, "y": 9},
              "length": 15,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb40",
              "name": "Enemy Snake",
              "health": 54,
              "body": [
                {"x": 2, "y": 0}, 
                {"x": 2, "y": 1}, 
                {"x": 2, "y": 2}
              ],
              "latency": "111",
              "head": {"x": 2, "y": 2},
              "length": 3,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 0, "y": 4}, 
                {"x": 1, "y": 4}, 
                {"x": 2, "y": 4},
                {"x": 2, "y": 3},
                {"x": 2, "y": 3},
                {"x": 3, "y": 3},
                {"x": 4, "y": 3}
              ],
              "latency": "111",
              "head": {"x": 4, "y": 3},
              "length": 7,
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
            {"x": 0, "y": 4}, 
            {"x": 1, "y": 4}, 
            {"x": 2, "y": 4},
            {"x": 2, "y": 3},
            {"x": 2, "y": 3},
            {"x": 3, "y": 3},
            {"x": 4, "y": 3}
          ],
          "latency": "111",
          "head": {"x": 4, "y": 3},
          "length": 7,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    
    expected_response = {'move': 'up', 'shout': 'I should move up'}
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertEqual(expected_response, response) 