from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Consumer, Distributor

# admin.site.register(User)
admin.site.register(Consumer)
admin.site.register(Distributor)
