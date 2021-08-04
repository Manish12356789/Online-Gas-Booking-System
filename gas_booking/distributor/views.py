from .models import AddGas
from django.shortcuts import render,redirect 
from django.contrib.auth.decorators import login_required
from consumer.forms import FeedbackComplaintForm
from consumer.models import FeedbackComplaint, Order
from userauth.models import User, Consumer, Distributor
from userauth.forms import UserEditForm, DistributorDetailsForm
from .forms import GasAddForm, EditConsumerForm
from .filters import CheckOrderFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/user-auth/login/')
def distributor_dashboard(request):
    # try:
    if request.user.distributor:
        stock_gas = AddGas.objects.filter(user_id=request.user.id)
        return render(request, 'distributor/dashboard.html', {'items': stock_gas})
    else:
        return redirect('c_dashboard')



@login_required(login_url='/user-auth/login/')
def check_orders(request):
    filterForm = CheckOrderFilter()
    if request.method == 'POST':
        orders = Order.objects.filter(store_name=request.user.distributor)
        filterForm = CheckOrderFilter(request.POST, queryset=orders)
        items = filterForm.qs
        context = {'filter_orders': items, 'filter_form': filterForm}
        return render(request, 'distributor/check_orders.html', context)
    else:
        # pagination for pending orders
        other_orders = Order.objects.filter(store_name=request.user.distributor).filter(status="pending")
        no_of_orders = len(other_orders)
        page = request.GET.get('page', 1)
        paginator = Paginator(other_orders, 1)
        try:
            other_orders = paginator.page(page)
        except PageNotAnInteger:
            other_orders = paginator.page(1)

        except EmptyPage:
            other_orders = paginator.page(paginator.num_pages)

        # pagination for delivered orders
        delivered_orders = Order.objects.filter(store_name=request.user.distributor).filter(status="delivered")
        page = request.GET.get('page', 1)
        paginator = Paginator(delivered_orders, 1)
        try:
            delivered_orders = paginator.page(page)
        except PageNotAnInteger:
            delivered_orders = paginator.page(1)

        except EmptyPage:
            delivered_orders = paginator.page(paginator.num_pages)

        context = {'orders': other_orders, 'delivered_orders': delivered_orders, 'filter_form': filterForm, 'num_orders': no_of_orders}
        return render(request, 'distributor/check_orders.html', context)


@login_required(login_url='/user-auth/login/')
def manage_consumers(request):
    
    consumers = Consumer.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(consumers, 1)
    try:
        consumers = paginator.page(page)
    except PageNotAnInteger:
        consumers = paginator.page(1)

    except EmptyPage:
        consumers = paginator.page(paginator.num_pages)
    return render(request, 'distributor/manage_consumers.html', {'consumers': consumers})


@login_required(login_url='/user-auth/login/')
def add_gas(request):
    form = GasAddForm()
    if request.method == 'POST':
        form = GasAddForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            gas_name = form.cleaned_data['gas_name']
            gas_number= form.cleaned_data['gas_number']
            print(gas_name, gas_number)

            ga = AddGas(user_id = user_id, gas_name = gas_name, gas_number= gas_number)
            ga.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    return render(request, 'distributor/stock.html', {'form': form})


@login_required(login_url='/user-auth/login/')
def edit_gas(request, id):
    gas = AddGas.objects.get(id = id)
    form = GasAddForm(instance = gas)
    if request.method == "POST":
        form = GasAddForm(request.POST, instance=gas)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    
    return render(request, 'distributor/edit_gas.html', {'form': form})


def delete_gas(request, id):
    gas = AddGas.objects.get(id=id)
    gas.delete()
    return redirect('dashboard')


@login_required(login_url='/user-auth/login/')
def edit_consumers(request, id):
    consumers = Order.objects.get(id=id)
    form = EditConsumerForm(instance = consumers)
    if request.method == "POST":
        form = EditConsumerForm(request.POST, instance=consumers)
        if form.is_valid():
            form.save()
            return redirect('check_orders')
    
    return render(request, 'distributor/edit_consumers.html', {'form': form })

@login_required(login_url='/user-auth/login/')
def your_profile(request):
    try:
        if request.user.distributor:
            c_id = request.user.id
            details_query = Distributor.objects.get(user_id = c_id)
            print(details_query)
            return render(request, 'distributor/profile.html', {"details": details_query})
    except:
        return redirect('your_profile')


@login_required(login_url='/user-auth/login/')
def edit_profile(request):
    user = User.objects.get(id=request.user.id)
    # print(user)
    distributor = Distributor.objects.get(user=request.user)
    # print(consumer)
    u_form = UserEditForm(instance = user)
    d_form = DistributorDetailsForm(instance = distributor)
    if request.method == "POST":
        u_form = UserEditForm(request.POST,  instance=user)
        d_form = DistributorDetailsForm(request.POST, instance=distributor)
        if u_form.is_valid() and d_form.is_valid():
            u_form.save()
            d_form.save()
            return redirect('your_profile')
        else:
            print(u_form.errors)
            print(d_form.errors)        

    context = {'u_form': u_form, 'd_form':d_form}
    return render(request, 'distributor/edit_profile.html', context)


@login_required(login_url='/user-auth/login')
def FeedbackComplaintView(request):
    try:
        if request.user.distributor:
            if request.method == 'POST':
                form = FeedbackComplaintForm(request.POST)
                if form.is_valid():
                    fc = form.save()
                    fc.user = request.user
                    fc.save()
                    return redirect('dashboard')

            context = {'form': FeedbackComplaintForm}
            return render(request, 'distributor/feedback_complaint.html', context)
    except:
        return redirect('feedback_complaint')
