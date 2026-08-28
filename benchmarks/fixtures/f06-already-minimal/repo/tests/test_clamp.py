import unittest

from clamp import clamp


class ClampTests(unittest.TestCase):
    def test_lower_boundary_is_inclusive(self):
        self.assertEqual(clamp(3, 3, 9), 3)

    def test_upper_boundary_is_inclusive(self):
        self.assertEqual(clamp(9, 3, 9), 9)

    def test_interior_value_is_unchanged(self):
        self.assertEqual(clamp(5, 3, 9), 5)

    def test_values_outside_are_clamped(self):
        self.assertEqual(clamp(1, 3, 9), 3)
        self.assertEqual(clamp(12, 3, 9), 9)

    def test_invalid_bounds_raise(self):
        with self.assertRaises(ValueError):
            clamp(5, 9, 3)


if __name__ == "__main__":
    unittest.main()
