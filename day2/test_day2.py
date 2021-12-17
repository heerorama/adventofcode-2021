import unittest
from day2 import challenge2
from day2 import feedChallenge2

class TestDay2(unittest.TestCase):
    def test_example2a(self):
        self.assertAlmostEqual(challenge2(['forward 5','down 5','forward 8','up 3','down 8','forward 2'], 'a'), 150)

    def test_2a(self):
       self.assertAlmostEqual(feedChallenge2('day2.txt', 'a'), 2117664)

    def test_example2b(self):
        self.assertAlmostEqual(challenge2(['forward 5','down 5','forward 8','up 3','down 8','forward 2'], 'b'), 900)

    def test_2b(self):
        self.assertAlmostEqual(feedChallenge2('day2.txt', 'b'), 2073416724)

