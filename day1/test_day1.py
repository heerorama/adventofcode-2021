import unittest
from day1 import challenge1a
from day1 import feedChallenge1a
from day1 import challenge1b
from day1 import feedChallenge1b

class TestDay1(unittest.TestCase):
    def test_example1a(self):
        self.assertAlmostEqual(challenge1a([199,200,208,210,200,207,240,269,260,263]), 7)

    def test_1a(self):
        self.assertAlmostEqual(feedChallenge1a('day1.txt'), 1316)

    def test_example1b(self):
        self.assertAlmostEqual(challenge1b([199,200,208,210,200,207,240,269,260,263]), 5)

    def test_1b(self):
        self.assertAlmostEqual(feedChallenge1b('day1.txt'), 1344)


