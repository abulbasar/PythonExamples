import unittest
from myapp import app

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_ping(self):
        self.assertTrue(app.ping() == "app")