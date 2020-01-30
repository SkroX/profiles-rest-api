from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps django with our custom user model"""

    def create_user(self,email,name,password=None):

        if not email:
            raise ValueError('user must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)

        user.save(using=self.db)

        return user


    def create_superuser(self,emal,name,password):
        """creates and saves a new super user"""

        user=self.create_user(self,emal,name,password)

        user.is_superuser=True
        user.is_staff=True

        user.save(using=self.db)

        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Represents a "user profile" inside our system."""


    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'

    REQUIRED_FIELD=['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """django uses this when object needed to be converted into string"""

        return self.email
