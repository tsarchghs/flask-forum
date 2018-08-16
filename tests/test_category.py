from application.views import app
import unittest
import os

class TestRoutes(unittest.TestCase):

    def setUp(self):
        app.config.from_object(os.environ.get('SETTINGS'))
        self.app = app.test_client()

    def test_showCategory(self):
        self.assertEqual((self.app.get("category/1")).status, '200 OK')
