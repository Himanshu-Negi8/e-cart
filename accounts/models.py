from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must Set a Password")

        user = self.model(
            email=self.normalize_email(email)

        )
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.set_password(password)  # change user password
        return user

    def create_staff_user(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff
    is_admin = models.BooleanField(default=False)  # superuser
    full_name = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return

    def get_short_name(self):
        return

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.is_admin

    @property
    def is_active(self):
        return self.is_active


