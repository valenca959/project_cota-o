from suppliers.models import Supplier
from fruits.models import Fruit
from quotes.models import Quote
from suppliers.serializers import SupplierSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['get'], url_path='fruits-with-prices')
    def fruits_with_prices(self, request, pk=None):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({"error": "Supplier not found"}, status=404)
        
        quotes = Quote.objects.filter(supplier=supplier).select_related('fruit').order_by('fruit__name')
        
        fruits_with_prices = [
            {
                "fruit_name": quote.fruit.name,
                "price": quote.price
            }
            for quote in quotes
        ]
        
        return Response({
            "supplier": supplier.name,
            "fruits_with_prices": fruits_with_prices
        })
