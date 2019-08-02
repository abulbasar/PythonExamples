import unittest
from myapp import db

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_ping(self):
        self.assertTrue(db.ping() == "db")