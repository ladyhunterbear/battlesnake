from battlesnake2.lib.coordinates.coordinate import Coordinate

class Snake:
    def __init__(self, snake):
        self.id = snake['id']
        self.name = snake['name']
        self.health = snake['health']
        self.body = []
        for body_coords in snake['body']:
            self.body.append(Coordinate(body_coords['x'], body_coords['y']))
        self.head = Coordinate(snake['head']['x'], snake['head']['y'])
        self.length = snake['length']
        self.latency = snake['latency']
        self.shout = snake['shout']
        if 'squad' in snake.keys():
            self.squad = snake['squad']
        
    def get_id(self) -> int:
        return self.id
        
    def get_name(self) -> str:
        return self.name
        
    def get_head(self) -> Coordinate:
        return self.head

    def get_body_coordinates(self):
        return self.body
        
    def get_health(self) -> int:
        return self.health

    '''
    Get snake length
    '''
    def get_length(self) -> int:
        return self.length
     
    '''
    Check if snake is alive.
    '''
    def is_alive(self) -> bool:
        return self.health > 0
        
    '''
    Check if snake is weaker.
    '''
    def is_weaker(self, snake) -> bool:
        return True if self.get_length() < snake.get_length() else False
          
    '''
    Check if snake is equal in health.
    '''
    def is_equal(self, snake) -> bool:
         return True if self.get_length() == snake.get_length() else False
      
    '''
    Check if snake has more health than my snake
    '''
    def is_healthier(self, snake) -> bool:
        return True if self.get_health() > snake.get_health() else False
    
