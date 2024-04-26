from django.test import LiveServerTestCase, TestCase
from .models import User, ForumPost, Member
from .views import create_post
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#----------------------------------------------------Selenium Testing--------------------------------------------------------------------------
class Hosttest(LiveServerTestCase):
    
    def testhomepage(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')
        assert 'Airsoft Multi-Tool' in driver.title

class LoginFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/accounts/login')

        user_name = driver.find_element(by='name', value='username')
        user_password = driver.find_element(by='name', value='password')
        submit = driver.find_element(by='id', value='submit')

        user_name.send_keys('testuser1')
        user_password.send_keys('minecraft1')
        submit.send_keys(Keys.RETURN)

        assert 'testuser1' in driver.page_source

class NewPostTestNoLogin(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/forum')

        new_post = driver.find_element(by='name', value='new')

        new_post.send_keys(Keys.RETURN)

        assert 'AMT - Login' in driver.title

class NewPostTestLoggedIn(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/accounts/login')

        user_name = driver.find_element(by='name', value='username')
        user_password = driver.find_element(by='name', value='password')
        submit = driver.find_element(by='id', value='submit')

        user_name.send_keys('testuser1')
        user_password.send_keys('minecraft1')
        submit.send_keys(Keys.RETURN)

        driver.get('http://127.0.0.1:8000/forum')

        new_post = driver.find_element(by='name', value='new')

        new_post.send_keys(Keys.RETURN)

        assert 'Create' in driver.page_source

#--------------------------------------------------------------Unit Tests---------------------------------------------------------------
class AuthenticationTest(TestCase):
 def setUp(self):
       User.objects.create(username='testuser')

 def test_user_created(self):
       user = User.objects.filter(username='testuser')
       self.assertTrue(user.exists())

class CreatePostTest(TestCase):
    def setUp(self):
        ForumPost.objects.create(title='testPost')

    def test_created_post(self):
        post = ForumPost.objects.filter(title='testPost')
        self.assertTrue(post.exists())

class UserRoleTest(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='testuser')

    def test_user_role(self):
        user = User.groups.filter(name='Members_Role')
        self.assertTrue(user.exists())
