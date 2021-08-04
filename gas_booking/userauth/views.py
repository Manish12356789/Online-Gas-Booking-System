from userauth.models import Distributor, Consumer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ConsumerDetailsForm, DistributorDetailsForm, UserForm, PasswordForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as dj_logout, update_session_auth_hash



def ConsumerSignupView(request):
	if request.user.is_authenticated:
		try:
			if request.user.consumer:
				return redirect('c_dashboard')
		except:
			if request.user.distributor:
				return redirect('dashboard')
	else:
		u_form = UserForm()
		c_form = ConsumerDetailsForm()
		if request.method == "POST":
			u_form = UserForm(request.POST)
			c_form = ConsumerDetailsForm(request.POST)

			if u_form.is_valid() and c_form.is_valid():
				user = u_form.save(commit=False)
				psw = u_form.cleaned_data['password']
				user.set_password(psw)
				user.save()
				u = User.objects.get(email = u_form.cleaned_data['email'])
				c = c_form.save(commit=False)
				print("This is c form run this instance")
				c.user = u
				c.save()
				return redirect('login')
			
			else:
				print(c_form.errors)
				print(u_form.errors)
		return render(request, 'userauth/sign_up.html', {'c_form': c_form, 'u_form':u_form})

def DistributorSignupView(request):
	if request.user.is_authenticated:
		try:
			if request.user.consumer:
				return redirect('c_dashboard')
		except:
			if request.user.distributor:
				return redirect('dashboard')
	else:
		u_form = UserForm()
		d_form = DistributorDetailsForm()
		if request.method == "POST":
			u_form = UserForm(request.POST)
			d_form = DistributorDetailsForm(request.POST)
			print(d_form)

			if u_form.is_valid() and d_form.is_valid():
				user = u_form.save(commit=False)
				psw = u_form.cleaned_data['password']
				image = request.FILES.get('proof_pic')
				user.proof_pic = image
				user.set_password(psw)
				user.save()
				u_id = User.objects.get(username = u_form.cleaned_data['username'])
				d = d_form.save(commit=False)
				d.user = u_id
				d.save()
				return redirect('login')

			else:
				print(u_form.errors)
				print(d_form.errors)
		return render(request, 'userauth/signup.html', {'d_form':d_form, 'u_form':u_form})


def login(request):

	if request.user.is_authenticated:
		try:
			if request.user.consumer:
				return redirect('c_dashboard')
		except:
			if request.user.distributor:
				return redirect('dashboard')
	else:
		if request.method == 'POST':
			phone = request.POST['username']
			password = request.POST['password']
			print('form is valid')
			print(phone, password)
			login_user = authenticate(username=phone, password=password)

			if login_user:
				auth_login(request, login_user)
				try:
					if request.user.consumer:
						return redirect('c_dashboard')
				except:
					if request.user.distributor:
				 		return redirect('dashboard')
			else:
				msg = messages.error(request, "Invalid Email or Password.")

		return render(request, "userauth/login.html")


@login_required(login_url='/user-auth/login/')
def logout(request):
    dj_logout(request)
    return redirect('/')



@login_required(login_url='/user-auth/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('logout')
        else:
            print(form.errors)
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'userauth/change_password.html', {
        'password_change_form': form
    })


