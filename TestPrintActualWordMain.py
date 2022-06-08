"""
Test module for rock paper scissors game printActualWord function
Author: Todimu Isewon
"""

import unittest
from main import printActualWord


class TestPrintActualWordMain(unittest.TestCase):
    """
        Test the function printActualWord from the module main.py
        To run tests in verbose mode, use the following command in terminal :
        python -m unittest -v TestPrintActualWordMain.py
    """

    # from the main.py file, I ensured that the inputs would be saved as lowercase
    # no matter what case was passed in

    def test_main_rock(self):
        self.assertEqual(printActualWord("r"), "rock")

    def test_main_paper(self):
        self.assertEqual(printActualWord("p"), "paper")

    def test_main_scissors(self):
        self.assertEqual(printActualWord("s"), "scissors")


if __name__ == "__main__":
    unittest.main()
