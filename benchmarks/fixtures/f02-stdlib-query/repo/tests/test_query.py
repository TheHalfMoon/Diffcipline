import unittest

from query import parse_query


class QueryTests(unittest.TestCase):
    def test_blank_query(self):
        self.assertEqual(parse_query(""), {})

    def test_decodes_repeated_and_blank_values(self):
        self.assertEqual(
            parse_query("q=hello+world&tag=a%2Fb&tag=c&empty="),
            {"q": ["hello world"], "tag": ["a/b", "c"], "empty": [""]},
        )


if __name__ == "__main__":
    unittest.main()
