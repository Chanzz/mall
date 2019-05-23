from . import models
from . import serializers
from rest_framework import generics


# Create your views here.
class CardealerView(generics.ListCreateAPIView):
    queryset = models.CarDealer.objects.all()
    serializer_class = serializers.CardealerSerializers


class CardealerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CarDealer.objects.all()
    serializer_class = serializers.CardealerSerializers


class CityView(generics.ListCreateAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializers


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializers


class ManufacturerNameView(generics.ListCreateAPIView):
    queryset = models.ManufacturerName.objects.all()
    serializer_class = serializers.ManufacturerNameSerializers


class ManufacturerNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ManufacturerName.objects.all()
    serializer_class = serializers.ManufacturerNameSerializers


class ProvinceView(generics.ListCreateAPIView):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializers


class ProvinceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Province.objects.all()
    serializer_class = serializers.ProvinceSerializers
