from django import forms
from django.forms import ModelForm
from .models import Kitchn

class KitchenForm(forms.ModelForm):

    class Meta:
        model = Kitchn
        fields =    [
                        "legal_name", 
                        "vendor_email", 
                        "address",
        ]


            

           
   