import unittest
from unittest.mock import patch
from io import StringIO
import runpy

class TestCalendar(unittest.TestCase):
    @patch("builtins.input", side_effect=["31", "1"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_calendar_prints_correct_output(self, mock_stdout, mock_input):
        runpy.run_path("Calendar.py", run_name="__main__")
        output = mock_stdout.getvalue()

        # Check expected lines
        self.assertIn("S  M  T  W  T  F  S", output)
        self.assertIn("1   2   3   4   5   6   7", output)
        self.assertIn("8   9  10  11  12  13  14", output)
        self.assertIn("15  16  17  18  19  20  21", output)
        self.assertIn("22  23  24  25  26  27  28", output)
        self.assertIn("29  30  31", output)

if __name__ == "__main__":
    unittest.main()


