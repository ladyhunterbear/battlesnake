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
                {"x": 10, "y": 9}
              ],
              "latency": "111",
              "head": {"x": 10, "y": 8},
              "length": 2,
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
    
    
  def test_snake_avoid_stronger_snake(self):
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
            {"x": 3, "y": 9}
          ],
          "hazards": [],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 50,
              "body": [
                {"x": 5, "y": 9}, 
                {"x": 6, "y": 9}, 
                {"x": 6, "y": 10},
                {"x": 7, "y": 10},
                {"x": 7, "y": 9},
                {"x": 7, "y": 8},
                {"x": 7, "y": 7},
                {"x": 6, "y": 7}
              ],
              "latency": "111",
              "head": {"x": 5, "y": 9},
              "length": 8,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb38",
              "name": "Enemy Snake",
              "health": 50,
              "body": [
                {"x": 1, "y": 9}, 
                {"x": 1, "y": 10}, 
                {"x": 0, "y": 10},
                {"x": 0, "y": 9}, 
                {"x": 0, "y": 8}, 
                {"x": 0, "y": 7},
                {"x": 0, "y": 6},
                {"x": 0, "y": 5},
                {"x": 0, "y": 4}
                
              ],
              "latency": "111",
              "head": {"x": 1, "y": 9},
              "length": 9,
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
            {"x": 5, "y": 9}, 
            {"x": 6, "y": 9}, 
            {"x": 6, "y": 10},
            {"x": 7, "y": 10},
            {"x": 7, "y": 9},
            {"x": 7, "y": 8},
            {"x": 7, "y": 7},
            {"x": 6, "y": 7}
          ],
          "latency": "111",
          "head": {"x": 5, "y": 9},
          "length": 8,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    expected_responses = [
      {'move': 'down', 'shout': 'I should move down'},
      {'move': 'up', 'shout': 'I should move up'}
    ]
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertTrue(response in expected_responses)
    
  def test_snake_dont_fight_equal_snake_for_food(self):
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
            {"x": 5, "y": 5}
          ],
          "hazards": [],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 50,
              "body": [
                {"x": 1, "y": 5}, 
                {"x": 2, "y": 5}, 
                {"x": 2, "y": 6},
                {"x": 3, "y": 6},
                {"x": 3, "y": 5}
              ],
              "latency": "111",
              "head": {"x": 3, "y": 5},
              "length": 5,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb38",
              "name": "Enemy Snake",
              "health": 50,
              "body": [
                {"x": 4, "y": 4}, 
                {"x": 4, "y": 3}, 
                {"x": 3, "y": 3},
                {"x": 3, "y": 2}, 
                {"x": 3, "y": 1}   
              ],
              "latency": "111",
              "head": {"x": 4, "y": 4},
              "length": 5,
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
            {"x": 1, "y": 5}, 
            {"x": 2, "y": 5}, 
            {"x": 2, "y": 6},
            {"x": 3, "y": 6},
            {"x": 3, "y": 5}
          ],
          "latency": "111",
          "head": {"x": 3, "y": 5},
          "length": 5,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    expected_responses = [
      {'move': 'down', 'shout': 'I should move down'},
      {'move': 'right', 'shout': 'I should move right'}
    ]
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    self.assertTrue(response in expected_responses)