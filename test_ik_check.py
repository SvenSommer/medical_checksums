import unittest
from ik_check import calculate_checksum, validate_ik
from ik_values import positives

negatives = [131280116, 131180067]

class TestIKCheck(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum("26032682"), 2)
        self.assertEqual(calculate_checksum("27060018"), 6)

    def test_is_valid_ik_number(self):
        for validIk in positives:
            self.assertTrue(validate_ik(str(validIk)))

        for invalidIk in negatives:
            self.assertFalse(validate_ik(str(invalidIk)))

if __name__ == '__main__':
    unittest.main()



