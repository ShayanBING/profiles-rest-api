from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin

class UserProfile(AbstractBaseUser,PermissionMixin):
    """Data Base models for users in the systems"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrive full name of user"""
        return self.name

    def get_short_name(self):
        """retrive short name of user"""
        return self.name

    def __str__ (self):
        """return string representation of our user"""
        return self.email

    
