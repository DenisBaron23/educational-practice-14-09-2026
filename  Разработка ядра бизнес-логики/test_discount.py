import unittest

from discount import calculate_partner_discount


class TestCalculatePartnerDiscount(unittest.TestCase):
    def test_negative_quantity_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            calculate_partner_discount(-1)

    def test_discount_for_9999(self) -> None:
        self.assertEqual(calculate_partner_discount(9999), 0)

    def test_discount_for_10000(self) -> None:
        self.assertEqual(calculate_partner_discount(10000), 5)

    def test_discount_for_49999(self) -> None:
        self.assertEqual(calculate_partner_discount(49999), 5)

    def test_discount_for_50000(self) -> None:
        self.assertEqual(calculate_partner_discount(50000), 10)

    def test_discount_for_299999(self) -> None:
        self.assertEqual(calculate_partner_discount(299999), 10)

    def test_discount_for_300000(self) -> None:
        self.assertEqual(calculate_partner_discount(300000), 15)


if __name__ == "__main__":
    unittest.main()
