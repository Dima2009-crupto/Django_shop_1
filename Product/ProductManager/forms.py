from django import forms
from .models import Product



class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=150, label='Product Name', widget = forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.IntegerField(label='Price', widget = forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget = forms.Textarea(attrs={'class': 'form-control'}))


    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']