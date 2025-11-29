import unittest
from my_calendar import generate_calendar

class TestCalendar(unittest.TestCase):
    def test_starting_on_sunday(self):
        output = generate_calendar(31, 1)
        expected = (
            "S  M  T  W  T  F  S\n"
            " 1  2  3  4  5  6  7\n"
            " 8  9 10 11 12 13 14\n"
            "15 16 17 18 19 20 21\n"
            "22 23 24 25 26 27 28\n"
            "29 30 31"
        )
        self.assertEqual(output, expected)

if __name__ == "__main__":
    unittest.main()



