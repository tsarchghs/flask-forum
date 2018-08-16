from application.views import app
import unittest
import os

class TestRoutes(unittest.TestCase):

    def setUp(self):
        app.config.from_object(os.environ.get('SETTINGS'))
        self.app = app.test_client()

    def test_status_codes(self):
        self.assertEqual((self.app.get('/auth/login')).status, '200 OK')
        self.assertEqual((self.app.get('/auth/register')).status, '200 OK')
