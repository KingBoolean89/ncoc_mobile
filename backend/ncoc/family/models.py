from django.db import models
from django.utils.timezone import now


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=75)
    event_type = models.CharField(max_length=50)
    start_time = models.DateTimeField(default=now, null=True, blank=True)
    end_time = models.DateTimeField(default=now, null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __repr__(self):
        return self.title


class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    events = models.ManyToManyField(Event, related_name='child', blank=True)


def __repr__(self):
    return self.first_name
