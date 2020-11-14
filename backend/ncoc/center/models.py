from django.db import models
from family.models import Child
from user.models import User


# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=100)
    portion = models.CharField(max_length=75)

    def __repr__(self):

        self.name


class Center(models.Model):
    name = models.CharField(max_length=100)

    def __repr__(self):
        self.name


class DailyReport(models.Model):
    title = models.CharField(max_length=75)
    date = models.DateField(auto_now=True)
    large_group = models.TextField()
    small_group = models.TextField(blank=True, null=True)
    centers = models.ManyToManyField(
        Center, related_name='reports')
    story = models.TextField(blank=True, null=True)
    art = models.TextField(blank=True, null=True)
    music = models.TextField(blank=True, null=True)
    needed_items = models.TextField()
    meals = models.ManyToManyField(
        Meal,  related_name='reports')
    child = models.ForeignKey(
        Child, on_delete=models.DO_NOTHING, related_name='reports')
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='reports')

    def __repr__(self):
        self.title
