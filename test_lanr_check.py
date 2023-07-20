import unittest
from lanr_check import calculate_checksum, validate_lanr
from lanr_values import positives, negatives

class TestLANRCheck(unittest.TestCase):
    def test_calculate_checksum(self):
        self.assertEqual(calculate_checksum("123456"), 4)
        self.assertEqual(calculate_checksum("987654"), 2)
        self.assertEqual(calculate_checksum("545878"), 9)
        self.assertEqual(calculate_checksum("444444"), 2) #4 Pseudoarztnummer im Rahmen des Reha-Entlassmanagements noch verwendet
        self.assertEqual(calculate_checksum("999999"), 6) #9 Hochschulambulanzen nach § 117 SGB V sowie psychiatrische und psychosomatische Institutsambulanzen nach § 118 SGB V und einige weitere Ambulanztypen
        self.assertEqual(calculate_checksum("999999"), 6) #9 Pseudoarztnummer im Rahmen des Reha-Entlassmanagements noch verwendet



    def test_validate_lanr(self):
        self.assertTrue(validate_lanr("545878998"))
        self.assertTrue(validate_lanr("444444400")) # Pseudoarztnummer im Rahmen des Reha-Entlassmanagements noch verwendet
        self.assertTrue(validate_lanr("999999900")) # Hochschulambulanzen nach § 117 SGB V sowie psychiatrische und psychosomatische Institutsambulanzen nach § 118 SGB V und einige weitere Ambulanztypen
        self.assertTrue(validate_lanr("999999991")) # Zahnärzte in zahnärztlichen Hochschulambulanzen
        self.assertTrue(validate_lanr("123456435"))
        self.assertTrue(validate_lanr("000000000"))
        self.assertTrue(validate_lanr("5555550012"))
        self.assertFalse(validate_lanr("123456621"))

    def test_is_valid_lanr(self):
        for validIk in positives:
            self.assertTrue(validate_lanr(str(validIk)))

        for invalidIk in negatives:
            self.assertFalse(validate_lanr(str(invalidIk)))


if __name__ == '__main__':
    unittest.main()