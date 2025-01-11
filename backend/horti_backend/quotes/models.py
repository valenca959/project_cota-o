from django.db import models
from suppliers.models import Supplier
from fruits.models import Fruit

# Create your models here.
class Quote(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='quotes')
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE, related_name='quotes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.supplier} - {self.fruit} - R${self.price}'