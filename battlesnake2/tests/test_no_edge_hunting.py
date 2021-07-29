from django.test import TestCase
from battlesnake2.game import Game
import json

# Only test cases with 1 obvious outcome. 

class BattleSnake2NoEdgeHuntingTestCase(TestCase):
  def test_snake_does_not_hunt_on_edge(self):
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
              "name": "Opponent Snake",
              "health": 54,
              "body": [
                {"x": 6, "y": 2}, 
                {"x": 6, "y": 1}, 
                {"x": 7, "y": 1},
                {"x": 8, "y": 1},
                {"x": 9, "y": 1}
              ],
              "latency": "111",
              "head": {"x": 9, "y": 1},
              "length": 5,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 5, "y": 0}, 
                {"x": 5, "y": 1}, 
                {"x": 5, "y": 2},
                {"x": 5, "y": 3},
                {"x": 5, "y": 4},
                {"x": 5, "y": 5}
              ],
              "latency": "111",
              "head": {"x": 5, "y": 0},
              "length": 6,
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
            {"x": 5, "y": 0}, 
            {"x": 5, "y": 1}, 
            {"x": 5, "y": 2},
            {"x": 5, "y": 3},
            {"x": 5, "y": 4},
            {"x": 5, "y": 5}
          ],
          "latency": "111",
          "head": {"x": 5, "y": 0},
          "length": 6,
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
    
  def test_snake_hunts_not_on_edge(self):
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
              "name": "Opponent Snake",
              "health": 54,
              "body": [
                {"x": 6, "y": 3}, 
                {"x": 6, "y": 2}, 
                {"x": 7, "y": 2},
                {"x": 8, "y": 2},
                {"x": 9, "y": 2}
              ],
              "latency": "111",
              "head": {"x": 9, "y": 2},
              "length": 5,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 5, "y": 1}, 
                {"x": 5, "y": 2}, 
                {"x": 5, "y": 3},
                {"x": 5, "y": 4},
                {"x": 5, "y": 5},
                {"x": 5, "y": 6}
              ],
              "latency": "111",
              "head": {"x": 5, "y": 1},
              "length": 6,
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
            {"x": 5, "y": 2}, 
            {"x": 5, "y": 3}, 
            {"x": 5, "y": 4},
            {"x": 5, "y": 5},
            {"x": 5, "y": 6},
            {"x": 5, "y": 7}
          ],
          "latency": "111",
          "head": {"x": 5, "y": 2},
          "length": 6,
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
