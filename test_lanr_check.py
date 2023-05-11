import unittest
from lanr_check import calculate_checksum, validate_lanr

class TestLANRCheck(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum("123456"), 4)
        self.assertEqual(calculate_checksum("987654"), 2)
        self.assertEqual(calculate_checksum("545878"), 9)

    def test_validate_lanr(self):
        self.assertTrue(validate_lanr("545878998"))
        self.assertTrue(validate_lanr("123456435"))
        self.assertFalse(validate_lanr("123456621"))

if __name__ == '__main__':
    unittest.main()