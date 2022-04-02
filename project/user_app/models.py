from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=127)


class City(models.Model):
    name = models.CharField(max_length=127)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.PositiveSmallIntegerField()
    sex = models.BooleanField()
    username = None

    city = models.ForeignKey('user_app.City', models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('user_app.Tag', related_name='users', blank=True)
    subscriptions = models.ManyToManyField('user_app.User', related_name='subscribers')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
