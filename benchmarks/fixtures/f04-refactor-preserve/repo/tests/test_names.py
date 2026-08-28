import inspect
import unittest

import names


class NameTests(unittest.TestCase):
    def test_public_normalizers_preserve_behavior(self):
        self.assertEqual(names.normalize_first("  ADA   Lovelace "), "ada lovelace")
        self.assertEqual(names.normalize_last("  DE   MORGAN "), "de morgan")

    def test_same_person_uses_normalized_values(self):
        self.assertTrue(names.same_person(" Ada ", "LOVELACE", "ada", " lovelace "))

    def test_normalization_rule_has_one_casefold_site(self):
        self.assertEqual(inspect.getsource(names).count(".casefold()"), 1)


if __name__ == "__main__":
    unittest.main()
