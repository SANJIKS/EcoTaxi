from rest_framework import serializers
from .models import Driver

class DriverLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('current_latitude', 'current_longitude',)