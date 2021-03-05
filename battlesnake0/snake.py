from battlesnake0.coordinate import Coordinate

class Snake:
    def __init__(self, snake):
        self.id = snake['id']
        self.name = snake['name']
        self.health = snake['health']
        self.body = {}
        for coords in snake['body']:
            self.body[self.get_key(coords['x'], coords['y'])] = Coordinate(coords['x'], coords['y'])
        self.latency = snake['latency']
        self.head = Coordinate(snake['head']['x'], snake['head']['y'])
        self.length = snake['length']
        self.shout = snake['shout']
        self.squad = snake['squad']

    def get_key(self, x, y):
        key = str(x) + "_" + str(y)
        return key

    def get_id(self):
        return self.id

    def get_head(self):
        return self.head

    def get_body_coordinates(self):
        return self.body