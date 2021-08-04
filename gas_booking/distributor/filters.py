from django.db.models import fields
from consumer.models import Order
from userauth.models import Consumer, User
import django_filters
from django_filters import ModelChoiceFilter, widgets, DateFromToRangeFilter, ChoiceFilter
from .models import *
from django import forms




class CheckOrderFilter(django_filters.FilterSet):
    STATUS = [
        ('delivered', 'Delivered'),
        ('pending', 'Pending'),
    ]
    USER_CHOICE = []
    GAS_CHOICES = []
    user_id = Order.objects.values_list('user', flat=True).distinct()
    gas_id = Order.objects.values_list('gas_name', flat=True).distinct()
    
    print(user_id)
    for id in user_id:
        users = User.objects.filter(id=id).values_list('first_name', 'last_name')
        print(users)
        for user in users:
            print(user)
            full_name = ' '.join([''.join(sub) for sub in user])
            print(full_name)
            USER_CHOICE.append((id, full_name))

    for id in gas_id:
        choice = AddGas.objects.filter(id=id).values_list('gas_name', flat=True)
        for ch in choice:
            GAS_CHOICES.append((id, ch))

    order_date = DateFromToRangeFilter(field_name='order_date', lookup_expr='gte', label='Select Order Date:',
     widget =  widgets.RangeWidget(attrs={
            'type': 'date',
            'class': 'form-control'
        }) )

    user = ChoiceFilter(choices = USER_CHOICE, label = "Consumer's Name:",
    widget = forms.Select(attrs={
        'class': 'form-select',
    }) )

    gas_name = ChoiceFilter(choices = GAS_CHOICES,
    widget = forms.Select(attrs={
        'class': 'form-select',
    }) )

    status = ChoiceFilter(choices = STATUS, widget = forms.Select(attrs={'class': 'form-select'}))
    class Meta:
        model = Order
        fields = ['order_date', 'user', 'gas_name', 'status']