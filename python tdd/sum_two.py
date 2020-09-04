import unittest

def sum_two(a, b):
    return a + b

#commandline: python -m unittest sum_two.py

class MainTest(unittest.TestCase):

    def test_sum_two(self):
        test_value = sum_two(3, 4)
        self.assertEqual(test_value, 7)