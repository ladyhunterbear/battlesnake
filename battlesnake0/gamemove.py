from battlesnake0.gameboard import GameBoard, GameBoardSquare, GameBoardSquareState, GameBoardSquareNextState
from random import *


class GameMove:
    gameboard: GameBoard = None
    
    def __init__(self, gameboard):
        self.gameboard = gameboard
 

    def get_left(self, x, y):
        new_x = x - 1
        if (new_x >= 0):
            return self.gameboard.squares[self.gameboard.get_key(new_x, y)]
        else:
            return False

    def get_right(self, x, y):
        new_x = x + 1
        if (new_x < self.gameboard.width):
            return self.gameboard.squares[self.gameboard.get_key(new_x, y)]
        else:
            return False

    def get_up(self, x, y):
        new_y = y - 1
        if (new_y >= 0):
            return self.gameboard.squares[self.gameboard.get_key(x, new_y)]
        else:
            return False        
        
    def get_down(self, x, y):
        new_y = y + 1
        if (new_y < self.gameboard.height):
            return self.gameboard.squares[self.gameboard.get_key(x, new_y)]
        else:
            return False

    def can_move_square(self, square: GameBoardSquare):
        state = square.get_state()
        if (state == GameBoardSquareState.SNAKE_ENEMY_BODY):
            return False
        elif (state == GameBoardSquareState.SNAKE_ENEMY_HEAD):
            return False
        elif (state == GameBoardSquareState.SNAKE_SELF_BODY):
            return False
        elif (state == GameBoardSquareState.HAZARD):
            return False
        elif (state == GameBoardSquareState.EMPTY):
            return True
        elif (state == GameBoardSquareState.FOOD):
            return True
        else:
            return False
           
    def can_move(self, direction, x, y):
        target_square = None
        if (direction == 'up'):
            target_square = self.get_up(x, y)
        elif (direction == 'down'):
            target_square = self.get_down(x, y)
        elif (direction == 'left'):
            target_square = self.get_left(x, y)
        elif (direction == 'right'):
            target_square = self.get_right(x, y)
            
        if (target_square == False):
            return False
        else:
            return target_square if self.can_move_square(target_square) else False
    
    def can_move_next(self, square: GameBoardSquare):
        ok_next_states = [
            GameBoardSquareNextState.I_CAN_MOVE,
            GameBoardSquareNextState.SMALLER_ENEMY_CAN_MOVE,
            GameBoardSquareNextState.ANYONE_CAN_MOVE,
        ]
        if (square.get_next_state() in ok_next_states):
            return True
        return False

    # should return the gamesquare itself? or update it?
    def get_possible_directions(self, snake):
        possible_directions = {}
        head_x = snake.get_head().get_x()
        head_y = snake.get_head().get_y()
        
        square_up = self.can_move('up', head_x, head_y)
        square_down = self.can_move('down', head_x, head_y)
        square_left = self.can_move('left', head_x, head_y)
        square_right = self.can_move('right', head_x, head_y)

        if (square_up):
            possible_directions['up'] = square_up
        if (square_down):
            possible_directions['down'] = square_down
        if (square_left):
            possible_directions['left'] = square_left 
        if (square_right):
            possible_directions['right'] = square_right

        return possible_directions

    def get_next_move_score(self, x, y):
        next_move_score = 0
        sq_up = self.can_move('up', x, y)
        sq_down = self.can_move('left', x, y)
        sq_left = self.can_move('right', x, y)
        sq_right = self.can_move('down', x, y)
        
        if sq_up and self.can_move_next(sq_up):
            next_move_score = next_move_score + 1
        if sq_down and self.can_move_next(sq_down):
            next_move_score = next_move_score + 1
        if sq_left and self.can_move_next(sq_left):
            next_move_score = next_move_score + 1        
        if sq_right and self.can_move_next(sq_right):
            next_move_score = next_move_score + 1
        return next_move_score


    def get_move(self):        
        for snake in self.gameboard.snakes:
            possible_game_squares = self.get_possible_directions(snake)
            for square in possible_game_squares:
                coords = possible_game_squares[square].get_coordinates()
                key = str(coords.get_x()) + "_" + str(coords.get_y())
                if (snake.length > self.gameboard.my_snake.length):
                    self.gameboard.squares[key].set_next_state(GameBoardSquareNextState.BIGGER_ENEMY_CAN_MOVE)
                elif (snake.length == self.gameboard.my_snake.length):
                    self.gameboard.squares[key].set_next_state(GameBoardSquareNextState.EQUAL_ENEMY_CAN_MOVE)
                elif (snake.length < self.gameboard.my_snake.length):
                    self.gameboard.squares[key].set_next_state(GameBoardSquareNextState.SMALLER_ENEMY_CAN_MOVE)

        my_possible_moves = self.get_possible_directions(self.gameboard.my_snake)
        for square in my_possible_moves:
            coords = my_possible_moves[square].get_coordinates()
            key = str(coords.get_x()) + "_" + str(coords.get_y())
            if (self.gameboard.squares[key].get_next_state() == GameBoardSquareNextState.EQUAL_ENEMY_CAN_MOVE):
                self.gameboard.squares[key].set_next_state(GameBoardSquareNextState.EQUAL_ENEMY_CAN_MOVE)
            elif (self.gameboard.squares[key].get_next_state() == GameBoardSquareNextState.SMALLER_ENEMY_CAN_MOVE):
                self.gameboard.squares[key].set_next_state(GameBoardSquareNextState.I_CAN_MOVE)
            elif (self.gameboard.squares[key].get_next_state() != GameBoardSquareNextState.BIGGER_ENEMY_CAN_MOVE):
                self.gameboard.squares[key].set_next_state(GameBoardSquareNextState.I_CAN_MOVE)

        choice = ''
        choice_score = 0
        for direction in my_possible_moves:
            x = my_possible_moves[direction].get_coordinates().get_x()
            y = my_possible_moves[direction].get_coordinates().get_y()

            my_possible_moves[direction].set_score(my_possible_moves[direction].get_score() + self.get_next_move_score(x, y))
            
            if my_possible_moves[direction].get_score() > choice_score:
                choice_score = my_possible_moves[direction].get_score()
                choice = direction
            elif my_possible_moves[direction].get_score() == choice_score:
                new_move = random() + self.get_next_move_score(my_possible_moves[direction].get_coordinates().get_x(), my_possible_moves[direction].get_coordinates().get_y())
                current_move = random() + self.get_next_move_score(my_possible_moves[choice].get_coordinates().get_x(), my_possible_moves[choice].get_coordinates().get_y())
                if (new_move > current_move):
                    choice_score = my_possible_moves[direction].get_score()
                    choice = direction
        
        board_matrix = self.gameboard.get_board_matrix()
        print(board_matrix)
        print(choice)
        response = {"move": choice, "shout": "I should move " + choice}    
        return response