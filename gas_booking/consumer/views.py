from django.contrib.auth.models import User
from distributor.models import AddGas
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from userauth.models import Distributor, Consumer
from userauth.forms import UserEditForm, ConsumerDetailsForm
from .models import Order,FeedbackComplaint
from .forms import FeedbackComplaintForm
from django.http import JsonResponse
from .filters import OrderHistoryFilter



@login_required(login_url='/user-auth/login/')
def dashboard(request):
    # try:
    #     if request.user.distributor:
    #        return redirect('dashboard')
    # except:
    # try:
    if request.user.consumer:
        distributor_details = Distributor.objects.all()
        return render(request, 'consumer/dashboard.html', {'distributor_details': distributor_details})
    else:
        return redirect('dashboard')
        

    
@login_required(login_url='/user-auth/login/')
def OrderView(request): 
    if request.method == "POST":
        distributor_name = request.POST.get('distributor_name')
        print(distributor_name)
        gas_name = request.POST.get('gas_name')
        print(gas_name)
        if distributor_name and gas_name:
            order = Order()
            order.user = request.user
            order.store_name_id = distributor_name
            order.gas_name_id = gas_name
            order.save()
            return redirect('order_history')

        distributor_id = request.POST.get('distributor_id')
        try:
            user = Distributor.objects.filter(id = distributor_id).first()
            names = AddGas.objects.filter(user_id = user.user_id)
        except Exception:
            data = {}
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(names.values('id', 'gas_name')), safe = False)
        

    distributors = Distributor.objects.all()
    context = {'distributors':distributors}
    return render(request, 'consumer/order.html', context)


        

        

@login_required(login_url='/user-auth/login/')
def OrderHistory(request):
    filterForm = OrderHistoryFilter()
    if request.method == "POST":
        filter_items = Order.objects.filter(user_id=request.user.id)
        filterForm = OrderHistoryFilter(request.POST, queryset=filter_items)
        items = filterForm.qs
        context = {'orders': items, 'filter_form': filterForm}
        return render(request, 'consumer/order_history.html', context)
        
    else:
        order_list = Order.objects.filter(user_id=request.user.id)
        context = {'orders': order_list, 'filter_form': filterForm}
        return render(request, 'consumer/order_history.html', context)

@login_required(login_url='/user-auth/login/')
def FeedbackComplaintView(request):
    try:
        if request.user.consumer:
            if request.method == 'POST':
                form = FeedbackComplaintForm(request.POST)
                if form.is_valid():
                    fc = form.save()
                    fc.user = request.user
                    fc.save()
                    return redirect('c_dashboard')

            context = {'form': FeedbackComplaintForm}
            return render(request, 'consumer/feedback_complaint.html', context)
    except:
        return redirect('d_feedback_complaint')



@login_required(login_url='/user-auth/login/')
def distributor_details(request, id):
    print(id)
    details_query = Distributor.objects.get(id = id)
    print(details_query)
    return render(request, 'consumer/distributor_details.html', {"details": details_query})


@login_required(login_url='/user-auth/login/')
def your_profile(request):
    try:
        if request.user.consumer:
            c_id = request.user.id
            details_query = Consumer.objects.get(user_id = c_id)
            print(details_query)
            return render(request, 'consumer/profile.html', {"details": details_query})
    except:
        return redirect('dis_profile')


@login_required(login_url='/user-auth/login/')
def edit_consumer(request):
    user = User.objects.get(id=request.user.id)
    # print(user)
    consumer = Consumer.objects.get(user=request.user)
    # print(consumer)
    u_form = UserEditForm(instance = user)
    c_form = ConsumerDetailsForm(instance = consumer)
    if request.method == "POST":
        u_form = UserEditForm(request.POST,  instance=user)
        c_form = ConsumerDetailsForm(request.POST, instance=consumer)
        if u_form.is_valid() and c_form.is_valid():
            u_form.save()
            c_form.save()
            return redirect('your_profile')
        else:
            print(u_form.errors)
            print(c_form.errors)        

    context = {'u_form': u_form, 'c_form':c_form}
    return render(request, 'consumer/edit_consumer.html', context)