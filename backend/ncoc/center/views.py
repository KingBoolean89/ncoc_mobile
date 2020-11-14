from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class MealViewset(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class CenterViewset(viewsets.ModelViewSet):
    queryset = Center.objects.all()
    serializer_classs = CenterSerializer


class DailyReportViewset(viewsets.ModelViewSet):
    queryset = DailyReport.objects.all()
    serializer_class = DailyReportSerializer
