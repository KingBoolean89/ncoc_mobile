from rest_framework import serializers
from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)

    class Meta:
        model = Child
        fields = ('first_name', 'last_name', 'dob', 'events')
