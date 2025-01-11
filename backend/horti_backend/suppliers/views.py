from suppliers.models import Supplier
from suppliers.serializers import SupplierSerializer
from rest_framework import ViewSet

class SupplierViewSet(ViewSet.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
