import unittest
from app import db
from app.models import User

class TestUserModel(unittest.TestCase):

    def test_is_authenticated(self):
        user = User(username='test_user', codigo_mesa=1)
        self.assertTrue(user.is_authenticated)

    def test_is_active(self):
        user = User(username='test_user', codigo_mesa=1)
        self.assertTrue(user.is_active)

