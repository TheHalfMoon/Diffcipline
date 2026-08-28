import unittest
from datetime import timezone

from timestamps import parse_timestamp


class TimestampTests(unittest.TestCase):
    def test_z_suffix_is_utc(self):
        parsed = parse_timestamp("2026-08-28T12:00:00Z")
        self.assertEqual(parsed.utcoffset(), timezone.utc.utcoffset(parsed))

    def test_normal_offset_is_preserved(self):
        parsed = parse_timestamp("2026-08-28T17:30:00+05:30")
        self.assertEqual(parsed.utcoffset().total_seconds(), 5.5 * 3600)

    def test_naive_timestamp_is_rejected(self):
        with self.assertRaises(ValueError):
            parse_timestamp("2026-08-28T12:00:00")


if __name__ == "__main__":
    unittest.main()
