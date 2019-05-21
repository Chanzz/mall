from rest_framework import serializers
from . import models


class CardealerSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.CarDealer
        fields = '__all__'
