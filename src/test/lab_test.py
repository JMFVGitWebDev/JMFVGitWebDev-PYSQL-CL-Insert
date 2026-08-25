import unittest

from src.main.lab import problem1

class TestInsertRecord(unittest.TestCase):

    def test_problem1(self):
        self.assertTrue(problem1())

if __name__ == "__main__":
    unittest.main()
