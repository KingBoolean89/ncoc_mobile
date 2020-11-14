from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from family.models import Child
# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    street1 = models.CharField(max_length=200)
    street2 = models.CharField(max_length=200)
    city = models.CharField(max_length=75)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    classroom = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    child = models.ManyToManyField(Child, related_name='parents', blank=True)

    def __repr__(self):
        self.email
