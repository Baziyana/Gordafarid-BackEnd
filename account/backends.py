from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class EmailPhoneAuthenticationBackend(object):
    """ login with email or phone_number """

    def authenticate(self, request, email_or_phone=None, password=None):
        try:
            user = User.objects.get(
                Q(email=email_or_phone) |
                Q(phone=email_or_phone)
            )

            if user and user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
