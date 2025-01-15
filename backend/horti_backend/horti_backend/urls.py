from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from fruits.views import FruitViewSet
from quotes.views import QuoteViewSet
from suppliers.views import SupplierViewSet

router = routers.DefaultRouter()

router.register(r'fruits', FruitViewSet, basename='fruits')
router.register(r'quotes', QuoteViewSet, basename='quotes')
router.register('suppliers', SupplierViewSet, basename='suppliers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
