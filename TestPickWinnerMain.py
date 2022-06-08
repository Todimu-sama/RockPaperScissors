"""
Test module for rock paper scissors game pickWinner function
Author: Todimu Isewon
"""

import unittest
from main import pickWinner


class TestPickWinnerMain(unittest.TestCase):

    """
    Test the function pickWinner from the module main.py
    To run tests in verbose mode, use the following command in terminal :
    >> python -m unittest -v TestPickWinnerMain.py
   """

    # from the main.py file, I ensured that the inputs would be saved as lowercase
    # no matter what case was passed in

    def test_main_tie_rock(self):
        self.assertEqual(pickWinner("r", "r"), "tie")

    def test_main_tie_paper(self):
        self.assertEqual(pickWinner("p", "p"), "tie")

    def test_main_tie_scissors(self):
        self.assertEqual(pickWinner("s", "s"), "tie")

    def test_main_win_rock(self):
        self.assertEqual(pickWinner("r", "s"), "r crushes s, you win !")

    def test_main_win_paper(self):
        self.assertEqual(pickWinner("p", "r"), "p covers r, you win !")

    def test_main_win_scissors(self):
        self.assertEqual(pickWinner("s", "p"), "s cuts p, you win !")

    def test_main_lose_rock(self):
        self.assertEqual(pickWinner("r", "p"), "r gets covered by p, computer wins")

    def test_main_lose_paper(self):
        self.assertEqual(pickWinner("p", "s"), "p gets cut by s, computer wins")

    def test_main_lose_scissors(self):
        self.assertEqual(pickWinner("s", "r"), "s gets crushed by r, computer wins")


if __name__ == "__main__":
    unittest.main()
