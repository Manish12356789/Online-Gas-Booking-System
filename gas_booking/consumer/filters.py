import django_filters
from django_filters import DateFromToRangeFilter, widgets
from django_filters.filters import ChoiceFilter
from .models import *
from django import forms



class OrderHistoryFilter(django_filters.FilterSet):
    STATUS = [
        ('delivered', 'Delivered'),
        ('pending', 'Pending'),
    ]

    # store_id = Order.objects.select_related('store_name').distinct()
    store_id = Order.objects.values_list('store_name', flat=True).distinct()
    # print(store_id)
    gas_id = Order.objects.values_list('gas_name', flat=True).distinct()
    STORE_CHOICES = []
    GAS_CHOICES = []

    for id in store_id:
        # print(id)
        choices = Distributor.objects.filter(id=id).values_list('distributor_name', flat=True)
        for choice in choices:
            # print(choice)
            STORE_CHOICES.append((id, choice))

    for id in gas_id:
        choice = AddGas.objects.filter(id=id).values_list('gas_name', flat=True)
        for ch in choice:
            GAS_CHOICES.append((id, ch))

    # print(STORE_CHOICES)
    # print(GAS_CHOICES)

    order_date = DateFromToRangeFilter(field_name='order_date', lookup_expr='gte', label='Select Order Date:',
     widget =  widgets.RangeWidget(attrs={
            'type': 'date',
            'class': 'form-control'
        }) )
   
    store_name = ChoiceFilter(choices = STORE_CHOICES, #  [{x.id, x.distributor_name} for x in STORE_CHOICES] 
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
        fields = ['order_date', 'store_name', 'gas_name', 'status']
        # widget = {
        #     'store_name': forms.Select(attrs={'class': 'form-select'})
        # }
        widgets = {
            'store_name': forms.Select(attrs={'class': 'form-control'}),
        }