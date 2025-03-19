from rest_framework import serializers
from .models import Device, SpeedRecord

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = 'all'

class SpeedRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedRecord
        fields = 'all'