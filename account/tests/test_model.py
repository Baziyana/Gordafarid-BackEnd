from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            email='user@test.com',
            username='user',
            phone_number='09999999999',
            full_name='test',
            description='test test test',
            password='123456789'

        )
        self.super_user = get_user_model().objects.create_superuser(
            email='test@test.com',
            username='superuser',
            phone_number='09999999998',
            full_name='test',
            description='test test test',
            password='123456789'
        )

    def test_str_method(self):
        self.assertEqual(str(self.user), self.user.email)
        self.assertEqual(str(self.super_user), self.super_user.email)

    def test_method_get_full_name(self):
        self.assertEqual(self.user.get_full_name, self.user.full_name)
        self.assertEqual(self.super_user.get_full_name, self.super_user.full_name)

    def test_field_phone_number(self):
        self.assertEqual(len(self.user.phone_number), 11)
        self.assertEqual(len(self.super_user.phone_number), 11)
