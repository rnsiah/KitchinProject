from django.contrib import admin
from .models import Kitchn, Meal, Order, Order_Item


admin.site.register(Kitchn)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Order_Item)
