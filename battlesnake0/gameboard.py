from enum import Enum
from battlesnake0.coordinate import Coordinate
from battlesnake0.snake import Snake
import numpy as np

class GameBoardSquareState(Enum):
        EMPTY = 1
        FOOD = 20
        SNAKE_SELF_BODY = 0
        SNAKE_SELF_HEAD = 0
        SNAKE_ENEMY_BODY = -2
        SNAKE_ENEMY_HEAD = -1
        HAZARD = 0
        NULL = 0

        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)


class GameBoardSquareNextState(Enum):
        I_CAN_MOVE = 10
        EQUAL_ENEMY_CAN_MOVE = 0
        BIGGER_ENEMY_CAN_MOVE = 0
        SMALLER_ENEMY_CAN_MOVE = 10
        ANYONE_CAN_MOVE = 1
        NO_ONE_CAN_MOVE = 0
        NULL = 0

        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)


class GameBoardSquare:
    state = GameBoardSquareState.NULL
    next_state = GameBoardSquareNextState.NULL
    coordinates = None
    score = 0
    # score should be hazard, me 
    def update_score(self):
        ok_state = [
            GameBoardSquareState.FOOD,
            GameBoardSquareState.EMPTY,
        ]
        can_move_states = [
            GameBoardSquareNextState.I_CAN_MOVE,
            GameBoardSquareNextState.ANYONE_CAN_MOVE,
            GameBoardSquareNextState.SMALLER_ENEMY_CAN_MOVE,
        ]
        if (self.state in ok_state and self.next_state in can_move_states):
            self.score = self.state.value + self.next_state.value
            return
        else:
            self.score = 0


    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def set_state(self, state: GameBoardSquareState):
        self.state = state
        self.update_score()
        
    def get_state(self):
        return self.state

    def set_next_state(self, next_state: GameBoardSquareNextState):
        self.next_state = next_state
        self.update_score()
        
    def get_next_state(self):
        return self.next_state

    def set_coordinates(self, coordinates: Coordinate):
        self.coordinates = coordinates

    def get_coordinates(self):
        return self.coordinates

    def __init__(self, coordinates: coordinates, state: GameBoardSquareState):
        self.set_coordinates(coordinates)
        self.set_state(state)
        if state == GameBoardSquareState.EMPTY or state == GameBoardSquareState.FOOD:
            self.set_next_state(GameBoardSquareNextState.ANYONE_CAN_MOVE)                
        elif state == GameBoardSquareState.HAZARD:
            self.set_next_state(GameBoardSquareNextState.NO_ONE_CAN_MOVE)
        elif state == GameBoardSquareState.SNAKE_ENEMY_BODY:
            self.set_next_state(GameBoardSquareNextState.NO_ONE_CAN_MOVE)
        elif state == GameBoardSquareState.SNAKE_ENEMY_HEAD:
            self.set_next_state(GameBoardSquareNextState.NO_ONE_CAN_MOVE)
        elif state == GameBoardSquareState.SNAKE_SELF_BODY:
            self.set_next_state(GameBoardSquareNextState.NO_ONE_CAN_MOVE)
        elif state == GameBoardSquareState.SNAKE_SELF_HEAD:
            self.set_next_state(GameBoardSquareNextState.NO_ONE_CAN_MOVE)
        self.update_score()

class GameBoard:
    board_size = 0
    height = 0
    width = 0
    squares = {}
    my_snake = None
    snakes = []
    
    def get_key(self, x, y):
        key = str(x) + "_" + str(y)
        return key

    def add_square(self, board_square: GameBoardSquare):
        x = board_square.coordinates.get_x()
        y = board_square.coordinates.get_y()
        self.squares[self.get_key(x, y)] = board_square

    def get_square(self, x, y): 
        return self.squares[self.get_key(x, y)]

    def update_square(self, x, y, state: GameBoardSquareState):
        key = self.get_key(x, y)
        self.squares[key].set_state(state)

    def get_board(self):
        return self.squares

    def add_food(self, food_squares):
        if (len(food_squares)):
            for food in food_squares:
                self.update_square(food['x'], food['y'], GameBoardSquareState.FOOD)

    def add_hazards(self, hazards):
        if (len(hazards)):
            for hazard in hazards:
                self.update_square(hazard['x'], hazard['y'], GameBoardSquareState.HAZARD)

    def add_my_snake(self, you):
        self.my_snake = Snake(you)
        for body_coords in self.my_snake.body:    
            x = self.my_snake.body[body_coords].get_x()
            y = self.my_snake.body[body_coords].get_y()
            self.update_square(x ,y , GameBoardSquareState.SNAKE_SELF_BODY)
        self.update_square(self.my_snake.head.get_x(), self.my_snake.head.get_y(), GameBoardSquareState.SNAKE_SELF_HEAD)

    def add_snakes(self, snakes):
        for snake in snakes:
            if (snake['id'] != self.my_snake.get_id()):
                enemy_snake = Snake(snake)
                self.snakes.append(enemy_snake)
                for body_coords in enemy_snake.body:    
                    x = enemy_snake.body[body_coords].get_x()
                    y = enemy_snake.body[body_coords].get_y()
                    self.update_square(x ,y , GameBoardSquareState.SNAKE_ENEMY_BODY)
                self.update_square(enemy_snake.head.get_x(), enemy_snake.head.get_y(), GameBoardSquareState.SNAKE_ENEMY_HEAD)

    def get_board_matrix(self):
        rows = []
        for i in range(self.height):
            rows.append([])
            for j in range(self.width):
                key = str(j) + "_" + str(i)
                rows[i].append(self.squares[key].get_score())
        rows.reverse()        
        board_matrix = np.array(rows)
        return board_matrix

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board_size = self.height * self.width
        for col in range(self.width):
            for row in range(self.height): 
                game_square = GameBoardSquare(Coordinate(row, col), GameBoardSquareState.EMPTY)
                self.add_square(game_square) 


