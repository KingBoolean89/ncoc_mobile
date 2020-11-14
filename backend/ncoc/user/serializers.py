from rest_framework import serializers
from .models import *
from family.serializers import ChildSerializer


class UserSerializer(serializers.ModelSerializer):
    child = ChildSerializer(many=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone', 'email',
                  'street1', 'city', 'state', 'zipcode', 'classroom', 'country', 'child')
