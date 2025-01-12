from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer
from rest_framework import viewsets


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
