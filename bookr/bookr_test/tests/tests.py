from django.test import TestCase, Client
from bookr_test.models import Publisher
from django.contrib.auth.models import User
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from bookr_test.views import greeting_view_user

# Create your tests here.

class TestPublisherModel(TestCase):
    """Test the publisher model."""
    def setUp(self):
        self.p = Publisher(name='Packt', website='www.packt.com', email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p), "Packt")


class TestGreetingView(TestCase):
    """Test the greeting view."""

    def setUp(self):
        self.client = Client()

    def test_greeting_view(self):
        response = self.client.get('/bookr_test/test/greeting/')
        self.assertEquals(response.status_code, 200)


class TestLoggedInGreetingView(TestCase):
    """Test the greeting view for the authenticated users."""

    def setUp(self):
        test_user= User.objects.create_user(username="testuser", password='test@#628password')
        test_user.save()
        self.client = Client()

    def test_user_greeting_not_authenticated(self):
        response = self.client.get('/bookr_test/test/greet_user/')
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        login = self.client.login(username='testuser', password='test@#628password')
        response = self.client.get('/bookr_test/test/greet_user/')
        self.assertEquals(response.status_code, 200)

class TestLoggedInGreetingViewRF(TestCase):
    """Test the greeting view for the authenticated users."""

    def setUp(self):
        self.test_user= User.objects.create_user(username="testuser", password='test@#628password')
        self.test_user.save()
        self.factory = RequestFactory()

    def test_user_greeting_not_authenticated(self):
        request = self.factory.get('/bookr_test/test/greet_user/')
        request.user = AnonymousUser()
        response = greeting_view_user(request)
        self.assertEquals(response.status_code, 302)

    def test_user_authenticated(self):
        request = self.factory.get('/bookr_test/test/greet_user/')
        request.user = self.test_user
        response = greeting_view_user(request)
        self.assertEquals(response.status_code, 200)
