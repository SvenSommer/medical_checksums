import unittest

from kvnr_check import calculate_checksum, validate_kvnr

class TestKVNRCheck(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum("T01234567"), 8)
        self.assertEqual(calculate_checksum("A98765432"), 0)
    def test_calculate_checksum(self):
        self.assertTrue(validate_kvnr("T012345678"))
        self.assertTrue(validate_kvnr("A000500015"))
        self.assertTrue(validate_kvnr("C000500021"))
        self.assertFalse(validate_kvnr("T012345679"))
        self.assertFalse(validate_kvnr("A0005000112"))
        self.assertFalse(validate_kvnr("C000500020"))




if __name__ == '__main__':
    unittest.main()





