from main.models import Product, Tag
from django import forms

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        #fields = ['__all__']
        exclude = []
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control form-control-lg mb-3'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Decription', 'class': 'form-control mb-3', 'style' : 'height: 100px'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Price($)', 'class': 'form-control form-control-lg mb-3', 'type' : 'number'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'placeholder': 'Quantity', 'class': 'form-control form-control-lg mb-3', 'type' : 'number'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'formFile', 'class': 'form-control mb-3', 'type' : 'file'}))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )