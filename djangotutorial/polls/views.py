from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Device, SpeedRecord
from .serializers import DeviceSerializer, SpeedRecordSerializer

class DeviceListView(APIView):
    def get(self, request):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeviceDetailView(APIView):
    def get(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def delete(self, request, device_id):
        device = get_object_or_404(Device, pk=device_id)
        device.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class SpeedRecordListView(APIView):
    def get(self, request):
        speed_records = SpeedRecord.objects.all()
        serializer = SpeedRecordSerializer(speed_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpeedRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpeedRecordDetailView(APIView):
    def get(self, request, record_id):
        record = get_object_or_404(SpeedRecord, pk=record_id)
        serializer = SpeedRecordSerializer(record)
        return Response(serializer.data)

    def delete(self, request, record_id):
        record = get_object_or_404(SpeedRecord, pk=record_id)
        record.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)