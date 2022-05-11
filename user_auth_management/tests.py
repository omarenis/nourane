from django.test import TestCase

# Create your tests here.
from user_auth_management.models import User
from user_auth_management.services import login


class AuthTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(firstname="nermine", lastname='ba3tout', email='nermineba3tout512@gmail.com')
        self.user.set_password('omar1996@+=')
        self.user.is_superuser = False
        self.user.save()

    def test_login(self):
        token = login(self.user.email, 'omar1996@+=')
        print(token)
        print(token.access_token)
