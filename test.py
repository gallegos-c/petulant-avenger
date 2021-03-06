
import unittest
from flask.ext.testing import TestCase
from flask.ext.login import current_user
from project import app, db
from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.add(BlogPost("Test post", "This is a test. Only a test.", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()



class FlaskTestCase(BaseTestCase):

	# Ensure that flask was setup properly
	def test_index(self):
		response = self.client.get('/login', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	# Ensure the main page requires login
	def test_main_route_requires_login(self):
		response = self.client.get('/', follow_redirects = True)
		self.assertTrue('Please log in to access this page.' in response.data)

	# Ensure that posts show up on the main page
	def test_post_show_up(self):
		response = self.client.post('/login', data = dict(username = "admin", password = "admin"), follow_redirects = True)
		self.assertIn('This is a test. Only a test.', response.data)


class usersViewsTests(BaseTestCase):

	# Ensure that login page loads correctly
	def test_login_page_loads(self):
		response = self.client.get('/login', content_type='html/text')
		self.assertTrue('Please login' in response.data)

	# Ensure that login behaves correctly with the correct credentials
	def test_correct_login(self):
		with self.client:
			response = self.client.post('/login', data = dict(username = "admin", password = "admin"), follow_redirects = True)
			self.assertIn('You were logged in.', response.data)
			self.assertTrue(current_user.name == "admin")
			self.assertTrue(current_user.is_active())

	# Ensure that login behaves correctly with the incorrect credentials
	def test_incorrect_login(self):
		response = self.client.post('/login', data = dict(username = "wrong", password = "wrong"), follow_redirects = True)
		self.assertIn('Invalid Credentials. please try again.', response.data)

	# Ensure that logout behaves correctly.
	def test_correct_logout(self):
		with self.client:
			self.client.post('/login', data = dict(username = "admin", password = "admin"), follow_redirects = True)
			response = self.client.get('/logout', follow_redirects = True)
			self.assertIn('You were logged out.', response.data)
			self.assertFalse(current_user.is_active())

	# Ensure that logout behaves correctly.
	def test_logout_route_requires_login(self):
		response = self.client.get('/logout', follow_redirects = True)
		self.assertIn('Please log in to access this page.', response.data)


	# Ensure user can register
	def test_user_registration(self):
		with self.client:
			response = self.client.post(
				'/register', 
				data = dict(username = "kloos123", email="kloos123@kloos.com", 
							password = "kloos123", confirm = "kloos123"), 
				follow_redirects = True
			)
			self.assertIn('Welcome to Flask!', response.data)
			self.assertTrue(current_user.name == "kloos123")
			self.assertTrue(current_user.is_active())

if __name__ == '__main__':
	unittest.main()