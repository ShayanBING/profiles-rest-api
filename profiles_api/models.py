from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager (BaseUserManager):
    """manager for user profiles"""
    def crate_user(self,email,name,password=None):
        """create a user profile"""
        if not emai :
            raise ValueError('User Must Have Value')
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_super_user(self,email,name,password):
        """create and save new super user(admin) with detailed info"""
        user = self.crate_user(email,name,password)
        user.is_superuser= True
        user.is_staff= True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
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
