import unittest
from unittest.mock import patch

import session


class SessionTests(unittest.TestCase):
    def test_active_before_expiry(self):
        value = session.Session("u", expires_at=11)
        self.assertTrue(session.is_active(value, 10))
        self.assertTrue(session.can_read(value, 10))
        self.assertTrue(session.can_write(value, 10))

    def test_exact_expiry_is_inactive_for_every_access_check(self):
        value = session.Session("u", expires_at=10)
        self.assertFalse(session.is_active(value, 10))
        self.assertFalse(session.can_read(value, 10))
        self.assertFalse(session.can_write(value, 10))

    def test_after_expiry_is_inactive(self):
        self.assertFalse(session.is_active(session.Session("u", 9), 10))

    def test_revoked_session_is_inactive(self):
        value = session.Session("u", expires_at=20, revoked=True)
        self.assertFalse(session.is_active(value, 10))
        self.assertFalse(session.can_read(value, 10))
        self.assertFalse(session.can_write(value, 10))

    def test_access_checks_delegate_to_single_active_policy(self):
        value = session.Session("u", expires_at=0)
        with patch("session.is_active", return_value=True) as active:
            self.assertTrue(session.can_read(value, 10))
            self.assertTrue(session.can_write(value, 10))
        self.assertEqual(active.call_count, 2)


if __name__ == "__main__":
    unittest.main()
