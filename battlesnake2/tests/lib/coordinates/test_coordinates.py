from django.test import TestCase
from battlesnake2.lib.coordinates.coordinate import Coordinate

class CoordinateTest(TestCase):
  def test_it_can_instantiate_new_coordinate(self):
    x = 1
    y = 2
    coord = new Coord(1,2)
    self.assertEqual(x, coord.get_x())
    self.assertEqual(y, coord.get_y())
    
    
  def test_it_update_change_coordinates(self):
    original_x = 1
    original_y = 2
    new_x = 3
    new_y = 4
    coord = new Coordinate(original_x, original_y)
    coord.set_x(new_x)
    coord.set_y(new_y)
    self.assertEqual(new_x, coord.get_x())
    self.assertEqual(new_y, coord.get_y())
    
  def test_it_returns_coordinate_as_string(self):
    x = 1
    y = 2
    expected = '1_2'
    coord = new Coordinate(x, y)
    self.assertEqual(expected, coord.stringify())