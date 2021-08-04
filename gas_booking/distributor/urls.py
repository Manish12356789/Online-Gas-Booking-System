from django.urls import path
from . import views
urlpatterns=[
    path('dashboard/', views.distributor_dashboard, name='dashboard'),
    path('feedback-complaint/', views.FeedbackComplaintView, name='d_feedback_complaint'),
    path('manage-consumers/', views.manage_consumers, name='manage_consumers'),
    path('check-orders/', views.check_orders, name='check_orders'),
    path('add-gas/', views.add_gas, name='add_gas'),
    path('edit-gas/<id>', views.edit_gas, name='edit_gas'),
    path('delete-gas/<id>', views.delete_gas, name='delete_gas'),
    path('edit_consumers/<id>', views.edit_consumers, name='edit_consumers'),
    path('your-profile/', views.your_profile, name='dis_profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),    

] 