from battlesnake2.lib.snakes.snake import Snake
from battlesnake2.lib.gameboard.gameboardsquarecollection import GameBoardSquareCollection
from battlesnake2.lib.enums.gameboardsquarestate import GameBoardSquareState
from battlesnake2.lib.gameboard.gameboardsquare import GameBoardSquare
from battlesnake2.lib.enums.opponentstrength import OpponentStrength

'''
Convert Snake classes to GameBoardSquareCollections
'''
class SnakeSquares:
    def __init__(self, my_snake: Snake, opponent: Snake = None):
        self.my_snake = my_snake
        self.opponent = opponent
    
    def get_squares(self) -> GameBoardSquareCollection:
        return self.get_my_snake() if self.opponent == None else self.get_opponent_snake()
            
    def get_my_snake(self) -> GameBoardSquareCollection:
        squares = GameBoardSquareCollection()
        body_coords = self.my_snake.get_body_coordinates()
        segement_counter = 1
        for body_coord in body_coords:
            if body_coord.stringify() == self.my_snake.get_head().stringify():
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_SELF_HEAD)
                squares.set(square)
            elif segement_counter == 1 or segement_counter == self.my_snake.get_length():
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_SELF_TAIL)
                squares.set(square)
            else:
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_SELF_BODY)
                squares.set(square)
            segement_counter = segement_counter + 1
        return squares
        
    def has_opponent(self) -> bool:
        return Snake == type(self.opponent)
    
    def get_opponent_snake(self) -> GameBoardSquareCollection:
        squares = GameBoardSquareCollection()
        segement_counter = 1
        body_coords = self.opponent.get_body_coordinates()
        
        for body_coord in body_coords:
            is_head = body_coord.stringify() == self.opponent.get_head().stringify()
            if is_head and self.get_opponent_strength() == OpponentStrength.WEAKER:    
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_WEAKER_ENEMY_HEAD)
                squares.set(square)
            elif is_head and self.get_opponent_strength() == OpponentStrength.EQUAL:
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_EQUAL_ENEMY_HEAD)
                squares.set(square)
            elif is_head and self.get_opponent_strength() == OpponentStrength.STRONGER:
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_STRONGER_ENEMY_HEAD)
                squares.set(square)
            elif (segement_counter == 1 and not is_head) or (segement_counter == self.opponent.get_length() and not is_head):
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_ENEMY_TAIL)
                squares.set(square)
            else:
                square = GameBoardSquare(body_coord, GameBoardSquareState.SNAKE_ENEMY_BODY)
                squares.set(square)
            segement_counter = segement_counter + 1
        return squares
            
    def get_opponent_strength(self) -> OpponentStrength:
        o = self.get_opponent_relative_length()
        
        if o == OpponentStrength.STRONGER:
            return OpponentStrength.STRONGER
        elif o == OpponentStrength.EQUAL:
            return OpponentStrength.EQUAL
        elif o == OpponentStrength.WEAKER:
            return OpponentStrength.WEAKER
            
    def get_opponent_relative_length(self) -> OpponentStrength:  
        if self.opponent.get_length() > self.my_snake.get_length():
            return OpponentStrength.STRONGER
        elif self.my_snake.get_length() == self.opponent.get_length():
            return OpponentStrength.EQUAL
        elif self.opponent.get_length() < self.my_snake.get_length():
            return OpponentStrength.WEAKER
                
    # def get_opponent_relative_health(self) -> OpponentStrength:
    #     if self.opponent.get_health() > self.my_snake.get_health():
    #         return OpponentStrength.STRONGER
    #     elif self.my_snake.get_health() == self.opponent.get_health():
    #         return OpponentStrength.EQUAL
    #     elif self.opponent.get_health() < self.my_snake.get_health():
    #         return OpponentStrength.WEAKER