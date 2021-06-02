from battlesnake2.lib.enums.coordinate import Coordinate

class Snake:
    def __init__(self, snake):
        self.id = snake['id']
        self.name = snake['name']
        self.health = snake['health']
        self.body = {}
        for body_coords in snake['body']:
            coord = Coordinate(body_coords['x'], body_coords['y'])
            self.body[coord.stringify()] = coord 
        self.latency = snake['latency']
        self.head = Coordinate(snake['head']['x'], snake['head']['y'])
        self.length = snake['length']
        self.shout = snake['shout']
        if 'squad' in snake.keys():
            self.squad = snake['squad']
        else:
            self.squad = ''

    def get_id(self):
        return self.id

    def get_head(self):
        return self.head

    def get_body_coordinates(self):
        return self.body
        
    def get_health(self):
        return self.health
        
    def get_length(self):
        return self.length
