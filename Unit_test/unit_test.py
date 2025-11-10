import unittest

# Function to test
def my_add(a, b):
    total = a + b
    return total

# Unit test class
class TestMyAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(my_add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(my_add(-2, -3), -5)

    def test_add_mixed_sign_numbers(self):
        self.assertEqual(my_add(-2, 3), 1)

    def test_add_with_zero(self):
        self.assertEqual(my_add(0, 5), 5)
        self.assertEqual(my_add(5, 0), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(my_add(2.5, 3.1), 5.6)

if __name__ == '__main__':
    unittest.main()
