from django import forms
from django.forms import ModelForm
from .models import Kitchn, Meal

class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchn
        fields =    [
                        "legal_name", 
                        "vendor_email", 
                        "address",
        ]


            
class MealForm(forms.ModelForm):
    
    class Meta:
        model = Meal
        fields = ['name', 'description', 'image_url', 'price']

