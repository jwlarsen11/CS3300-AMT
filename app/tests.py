from django.test import LiveServerTestCase, TestCase
from .models import User, ForumPost
from .forms import CreateUserForm, PostForm
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

class UserFormTest(TestCase):
    def test_invalid_data(self):
        data = {}
        f = CreateUserForm(data=data)
        self.assertFalse(f.is_valid())
        self.assertEquals(f.errors['password1'], ['This field is required.'])

    def test_valid_data(self):
        data = {'username': 'test', 'email': 'test@test.com', 'password1': 'testpass12', 'password2': 'testpass12'}
        f = CreateUserForm(data=data)
        self.assertTrue(f.is_valid())

class PostFormTest(TestCase):
    def test_invalid_data(self):
        data = {}
        f = PostForm(data=data)
        self.assertFalse(f.is_valid())
        self.assertEquals(f.errors['title'], ['This field is required.'])

    def test_valid_data(self):
        data = {'title':'testtitle', 'body':'testbody'}
        f = PostForm(data=data)
        self.assertTrue(f.is_valid())

class ViewTest(TestCase):
    def test_forum_view(self):
        response = self.client.get('/forum/')
        self.assertEquals(response.status_code, 200)