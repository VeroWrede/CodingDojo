import unittest
def min(l):
    # Should find and return minimum value in a given list
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100
### For this exercise, work within this class. This is something you will come up with on your own soon ###
class MainTest(unittest.TestCase):
    # tests go here!
    def test_min(self):
        test_value = min([2, 9, 3, 9, 7, -2])
        self.assertEqual(test_value, -2)

    def test_sum_lists (self):
        test_value = sum_list([2, 68, 78])
        self.assertEqual(test_value, 148)

    def test_less_than(self):
        test_value = less_than(900)
        self.assertFalse(test_value)