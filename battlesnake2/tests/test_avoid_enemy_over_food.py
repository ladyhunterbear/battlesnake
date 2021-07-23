from django.test import TestCase
from battlesnake2.game import Game
import json

# Only test cases with 1 obvious outcome. 

class BattleSnake2AvoidFoodWhenEnemyCloseTestCase(TestCase):
  def test_snake_does_seek_food_next_to_close_enemy(self):
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
            {"x": 6, "y": 1}
          ],
          "hazards": [],
          "snakes": [
            {
              "id": "snake-508e96ac-94ad-11ea-bb39",
              "name": "Opponent Snake",
              "health": 54,
              "body": [
                {"x": 0, "y": 0},
                {"x": 1, "y": 0},
                {"x": 2, "y": 0}, 
                {"x": 3, "y": 0}, 
                {"x": 4, "y": 0},
                {"x": 5, "y": 0}
                
              ],
              "latency": "111",
              "head": {"x": 5, "y": 0},
              "length": 6,
              "shout": "why are we shouting??",
              "squad": ""
            },
            {
              "id": "snake-508e96ac-94ad-11ea-bb37",
              "name": "My Snake",
              "health": 54,
              "body": [
                {"x": 7, "y": 2}, 
                {"x": 8, "y": 2}, 
                {"x": 8, "y": 3},
                {"x": 7, "y": 3},
                {"x": 6, "y": 3}
              ],
              "latency": "111",
              "head": {"x": 7, "y": 2},
              "length": 5,
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
            {"x": 7, "y": 2}, 
            {"x": 8, "y": 2}, 
            {"x": 8, "y": 3},
            {"x": 7, "y": 3},
            {"x": 6, "y": 3}
          ],
          "latency": "111",
          "head": {"x": 7, "y": 2},
          "length": 5,
          "shout": "why are we shouting??",
          "squad": ""
        }
      }
    '''
    expected_responses = [
      {'move': 'left', 'shout': 'I should move left'},
      {'move': 'down', 'shout': 'I should move down'}
    ]
    
     
    req = json.loads(request)
    game = Game(req)
    response = game.get_move()
    response_in_expected_responses = response in expected_responses
    self.assertTrue(response_in_expected_responses)
    
  