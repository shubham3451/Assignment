from django import forms
from .models import Order, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'special_instructions']

    quantity = forms.IntegerField(required=True, min_value=1)  # Make quantity mandatory
    order_date = forms.DateField(required=True, widget=forms.SelectDateWidget())  

    # Adding a date field to allow customers to select the order date
    order_date = forms.DateField(widget=forms.SelectDateWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()  # Fetch all available products
