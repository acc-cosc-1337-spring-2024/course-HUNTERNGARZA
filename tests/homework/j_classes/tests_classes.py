import unittest
from src.homework.j_classes.class_a import die

class Test_Config(unittest.TestCase):
    def test_rolling_class(self):
        for i in range(3):
            die_object = die()
            die_object.roll()
            self.assertIn(die_object.get_rolled_value(), range(1, 7))
