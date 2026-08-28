import tempfile
import unittest
from pathlib import Path

from storage import resolve_storage_path


class StorageTests(unittest.TestCase):
    def test_valid_nested_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            expected = (root / "team" / "report.txt").resolve()
            self.assertEqual(resolve_storage_path(root, "team/report.txt"), expected)

    def test_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            root.mkdir()
            with self.assertRaises(ValueError):
                resolve_storage_path(root, "../outside.txt")

    def test_absolute_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "root"
            root.mkdir()
            outside = (Path(tmp) / "outside.txt").resolve()
            with self.assertRaises(ValueError):
                resolve_storage_path(root, str(outside))

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp)
            root = base / "root"
            outside = base / "outside"
            root.mkdir()
            outside.mkdir()
            link = root / "linked"
            try:
                link.symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlink creation unavailable")
            with self.assertRaises(ValueError):
                resolve_storage_path(root, "linked/secret.txt")


if __name__ == "__main__":
    unittest.main()
