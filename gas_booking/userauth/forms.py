from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms
from django.forms import widgets
from .models import Consumer, Distributor
from django.contrib.auth import authenticate, login as auth_login, logout as dj_logout



class UserForm(forms.ModelForm):
    # password = forms.PasswordInput(attrs=({'type': 'password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs=({'type': 'password'}))

        }
        
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserEditForm(forms.ModelForm):
    # password = forms.PasswordInput(attrs=({'type': 'password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ConsumerDetailsForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Consumer
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'additional_information': forms.Textarea(attrs={'rows': 2, 'cols': 100}),
            'date_of_birth': forms.DateInput(attrs={'type':'date'}),
            'country': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super(ConsumerDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'




class DistributorDetailsForm(forms.ModelForm):
    class Meta:
        model = Distributor
        fields = '__all__'
        exclude = ['user', ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'additional_information': forms.Textarea(attrs={'rows': 2, 'cols': 100}),
            'proof_pic': forms.FileInput(attrs={'id': 'formFile'})
        }
    
    def __init__(self, *args, **kwargs):
        super(DistributorDetailsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super().save(commit=False)
    #     psw = self.cleaned_data["password"]
    #     user.set_password(psw)
    #     if commit:
    #         user.save()
    #     return user


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your Old Password...', 'data-toggle': 'password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your New Password...', 'data-toggle': 'password'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Your New Password...', 'data-toggle': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        

class PasswordResetFormWithError(PasswordResetForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'Enter your e-mail to reset password.'}))

    class Meta:
        fields = ['email']
       
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = ("There is no user registered with the specified E-Mail address.")
            self.add_error('email', msg)
        return email


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='', widget=forms.PasswordInput(
                                 attrs={'class': 'input--style-3', 'placeholder': 'Enter Your New Password...'}))
    new_password2 = forms.CharField(label='', widget=forms.PasswordInput(
                                    attrs={'class': 'input--style-3', 'placeholder': 'Confirm Your New Password...'}))
    class Meta:
        fields = ['new_password1', 'new_password2']