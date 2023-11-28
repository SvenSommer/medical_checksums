import unittest
from pzn_check import calculate_checksum, validate_pzn

class TestPZNCheck(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum("2758089"), 9)
        self.assertEqual(calculate_checksum("1234567"), 8)


    def test_validate_pzn(self):
       self.assertTrue(validate_pzn("12345678"))
       self.assertTrue(validate_pzn("15210588"))
       self.assertTrue(validate_pzn("12395133"))
       self.assertTrue(validate_pzn("00970810"))
       self.assertTrue(validate_pzn("04048914"))
       self.assertTrue(validate_pzn("04259775"))
       self.assertTrue(validate_pzn("04890568"))
       self.assertFalse(validate_pzn("12345671"))

    def test_pzn(self):
      # self.assertTrue(validate_pzn("444444411"))
      # self.assertTrue(validate_pzn("999999900"))
      # self.assertTrue(validate_pzn("555555"))
      # self.assertTrue(validate_pzn("000000000"))
     # self.assertTrue(validate_pzn("999999991"))
       self.assertTrue(validate_pzn("333333300"))

if __name__ == '__main__':
    unittest.main()