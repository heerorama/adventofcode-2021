import unittest
from day3 import counts_position_of_one
from day3 import generate_new_binary_code

class TestDay1(unittest.TestCase):
    def test_exampale_3a(self):
        self.assertAlmostEqual(generate_new_binary_code(['00100','11110','10110','10111','10101','01111','00111','1100','10000','11001','00010','01010']), 200)
