# tests/test_user_model.py

import unittest
from run import create_app, db
from app.models.user_model import User


class UserModelTestCase(unittest.TestCase):

    def setUp(self):
        # Create a new test app instance with a test configuration
        # You should define a 'testing' configuration
        self.app = create_app(config_name='TestingConfig')
        self.app_context = self.app.app_context() 
        # Push an application context to bind the SQLAlchemy object to your app
        self.app_context.push()
        db.create_all()  # Create all database tables

    def tearDown(self):
        db.session.remove()  # Remove the session
        db.drop_all()  # Drop all tables in the database
        self.app_context.pop()  # Remove the application context

    def test_password_hashing(self):
        u = User(username='john', email='john@example.com')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog')) 
        self.assertTrue(u.check_password('cat'))

    def test_avatar(self):
        # Add tests for any user model methods like avatar, etc.
        pass

    def test_unique_username_constraint(self):
        # Test to ensure that the username is unique
        u1 = User(username='john', email='john1@example.com')
        u2 = User(username='john', email='john2@example.com')
        db.session.add(u1)
        db.session.commit()
        with self.assertRaises(Exception):
            db.session.add(u2)
            db.session.commit()

    # Additional tests for other User model methods would go here


if __name__ == '__main__':
    unittest.main()
