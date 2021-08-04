from django.forms import widgets
from consumer.models import Order
# from django.forms import fields
from distributor.models import AddGas
from django import forms

# 'onChange': 'return validate(this);'
class GasAddForm(forms.ModelForm):
    class Meta:
        model = AddGas
        fields = '__all__'
        exclude = ['user',]
        widgets = {
            'gas_number': forms.NumberInput({'placeholder':'e.g. 1,2,...20,30..','class': 'form-control', 'id': 'gas_number'}),
            'gas_name': forms.TextInput({'placeholder':'e.g. LP Gas, Nepal Gas, etc.','class': 'form-control', 'id': 'gas_name'})
        }


class EditConsumerForm(forms.ModelForm):  
    class Meta:
        STATUS_CHOICE = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered')
    ]
        model = Order
        fields = ['payable_amount', 'status']
        widgets={
            'status': forms.Select(choices=STATUS_CHOICE, attrs={'class': 'form-select'}),
            'payable_amount': forms.NumberInput(attrs={'class':'form-control'})
        }