from rest_framework import serializers
from . import models


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class ManufacturerNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.ManufacturerName
        fields = '__all__'


class ProvinceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Province
        fields = '__all__'


class CardealerSerializers(serializers.ModelSerializer):
    # citys=CitySerializers(many=True,read_only=True)
    city_name = serializers.CharField(source='city.name')
    # province_name = serializers.CharField(source='province.name')
    # manufacturer_name=serializers.CharField(source='manufacturer_name.name')
    class Meta:
        model = models.CarDealer
        fields = '__all__'
        # depth = 1
