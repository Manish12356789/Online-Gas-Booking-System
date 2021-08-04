"""gas_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home.views import home
from userauth.views import ConsumerSignupView, login, logout
from consumer import urls as consumer_url
from distributor import urls as distributor_url
from userauth import urls as userauth_url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('logout/', logout, name='logout'),

    path('user-auth/', include(userauth_url)),
    path('consumer/', include(consumer_url)),
    path('distributor/', include(distributor_url)),
    # path('password/', include('django.contrib.auth.urls')),

]