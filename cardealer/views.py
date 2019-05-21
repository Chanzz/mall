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
