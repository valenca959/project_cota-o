from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/', include('fruits.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('quotes/', include('quotes.urls')),
]
