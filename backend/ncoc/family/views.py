from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ChildViewset(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
