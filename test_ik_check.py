import unittest
from ik_check import calculate_checksum, validate_ik

class TestIKCheck(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum("26032682"), 2)
        self.assertEqual(calculate_checksum("27060018"), 6)

    def test_is_valid_ik_number(self):
        self.assertTrue(validate_ik("107018414"))
        self.assertTrue(validate_ik("107018436"))
        self.assertFalse(validate_ik("131280116"))
        self.assertFalse(validate_ik("131180067"))

if __name__ == '__main__':
    unittest.main()



