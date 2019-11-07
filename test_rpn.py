import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)
    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_floor_div(self):
        result = rpn.calculate("12 8 /")
        self.assertEqual(1, result)
    def test_expo(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
