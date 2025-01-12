from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FruitViewSet


router = DefaultRouter()
router.register(r'fruits', FruitViewSet, basename='fruit')

urlpatterns = [
    path('', include(router.urls)),
]