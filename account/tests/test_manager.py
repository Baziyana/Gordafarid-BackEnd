from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagerTestCase(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='user@test.com',
            username='user',
            phone_number='09999999999',
            full_name='test',
            description='test test test',
            password='123456789'
        )

        self.assertIsInstance(user, get_user_model())
        self.assertFalse(user.is_staff, user.is_superuser)
        self.assertTrue(user.check_password)

    def test_create_super_user(self):
        superuser = get_user_model().objects.create_superuser(
            email='user@test.com',
            username='user',
            phone_number='09999999999',
            full_name='test',
            description='test test test',
            password='123456789'
        )
        self.assertIsInstance(superuser, get_user_model())
        self.assertTrue(superuser.is_staff, superuser.is_superuser)
        self.assertTrue(superuser.check_password)
