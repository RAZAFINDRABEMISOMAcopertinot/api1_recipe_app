from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_with_email_success(self):
        """" Test creating a new user with an email is successful.  """
        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email, 
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))