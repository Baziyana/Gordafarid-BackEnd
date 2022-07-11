from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from ckeditor_uploader import fields
from django.core.validators import RegexValidator


class CustomUserManager(UserManager):
    def _create_user(self, email, phone_number, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')
        if not phone_number:
            raise ValueError('Users must have an phone number address.')

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_number, password, **extra_fields):
        """ Create and save a user with the given phone_number and email """
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, phone_number, password, **extra_fields)

    def create_superuser(self, email, phone_number, password, **extra_fields):
        """ Create and save a super user with the given phone_number and email """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, phone_number, password, **extra_fields)


class CustomUser(AbstractUser):
    """ Custom User Model ==>  Email and Phone Number and password are required. Other fields are optional."""

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="شماره تلفن نامعتبر است .")
    full_name = models.CharField(max_length=350, blank=True, null=True, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(unique=True, verbose_name='پست الکترونیکی')
    phone_number = models.CharField(unique=True, max_length=11, validators=[phone_regex], verbose_name='شماره موبایل')
    avatar = models.ImageField(upload_to='uploads/Users/avatars', blank=True, null=True, verbose_name='عکس پروفایل')
    description = fields.RichTextUploadingField(blank=True, null=True,
                                                verbose_name="درباره من")  # from ckeditor #todo:RTL change

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username", 'full_name', "phone_number"]

    def get_full_name(self):
        """ return  full name user """
        return self.full_name
