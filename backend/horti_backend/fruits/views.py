from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from fruits.models import Fruit
from quotes.models import Quote
from fruits.serializers import FruitSerializer
from quotes.serializers import QuoteSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

    @action(detail=True, methods=['get'], url_path='suppliers-with-prices')
    def suppliers_with_prices(self, request, pk=None):
        try:
            fruit = Fruit.objects.get(pk=pk)
        except Fruit.DoesNotExist:
            return Response({"error": "Fruit not found"}, status=404)
        
        quotes = Quote.objects.filter(fruit=fruit).select_related('supplier').order_by('price')
        
        suppliers_with_prices = [
            {
                "supplier_name": quote.supplier.name,
                "price": quote.price
            }
            for quote in quotes
        ]
        
        return Response({
            "fruit": fruit.name,
            "suppliers_with_prices": suppliers_with_prices
        })
