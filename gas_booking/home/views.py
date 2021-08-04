from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from userauth.forms import UserForm


def home(request):
    form = UserForm()
    user = request.user
    if user.is_authenticated: 
        return redirect("dashboard")

    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         psw = form.cleaned_data['password']
    #         user.set_password(psw)
    #         user.save()
    #         return redirect('signup')

    return render(request, 'home/home.html')