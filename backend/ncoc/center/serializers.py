from rest_framework import serializers
from .models import *
from family.serializers import ChildSerializer
from user.serializers import UserSerializer


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = '__all__'


class DailyReportSerializer(serializers.ModelSerializer):
    centers = CenterSerializer(many=True)
    child = ChildSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = DailyReport
        fields = ('title', 'date', 'large_group', 'small_group', 'centers',
                  'story', 'arts', 'music', 'needed_items', 'meals', 'child', 'user')
