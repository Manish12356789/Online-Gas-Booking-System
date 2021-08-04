from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import PasswordForm, PasswordResetFormWithError, PasswordResetConfirmForm 
from . import views
urlpatterns=[
    path('distributor-signup/', views.DistributorSignupView, name='distributor_signup'),
    path('consumer-signup/', views.ConsumerSignupView, name='consumer_signup'),
    path('login/', views.login, name='login'),
    path('change_password/', views.change_password, name='change_password'),

    # password reset urls
     path('password/password_reset/', auth_views.PasswordResetView,
      name='password_reset'),
     path('password/password_reset/done',
          auth_views.PasswordResetDoneView.as_view(),
          name='password_reset_done'),
     path('password/reset/<uidb64>/<token>',
          auth_views.PasswordResetConfirmView,
          name='password_reset_confirm'),
     path('password/reset/done/',
          auth_views.PasswordResetCompleteView.as_view(),
          name='password_reset_complete'),

]