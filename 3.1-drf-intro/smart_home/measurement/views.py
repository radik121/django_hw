from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorDetail(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
