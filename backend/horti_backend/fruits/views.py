from rest_framework import viewsets
from fruits.models import Fruit
from fruits.serializers import FruitSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

