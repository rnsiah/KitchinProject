from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User


class Kitchn(models.Model):
    legal_name = models.CharField(max_length=50, blank=False, null=True)
    date_added=models.DateField(auto_now_add=True)
    vendor_email=models.EmailField(max_length=254, blank=False, null=True)
    address = models.CharField(max_length=200, blank=False, null =True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.legal_name
    
 


class Meal(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(blank=False, null=False)
    review = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.TextField(null= True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    kitchen=models.ForeignKey(Kitchn, on_delete=models.CASCADE, default=None, related_name='meals')

    def __str__(self):
        return self.name