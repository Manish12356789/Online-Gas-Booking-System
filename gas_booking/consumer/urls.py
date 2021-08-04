from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns=[
    path('dashboard/', views.dashboard, name='c_dashboard'),
    path('gas-order/', views.OrderView, name='gas_order'),
    path('order-history/', views.OrderHistory, name='order_history'),
    path('feedback-complaint/', views.FeedbackComplaintView, name='feedback_complaint'),
    path('distributors-details/<id>', views.distributor_details, name='distributor_details'),
    path('your-profile/', views.your_profile, name="your_profile"),
    path('terms-conditions/', TemplateView.as_view(template_name = 'consumer/order_terms_condition.html'), name='terms_conditions'),
    path('edit-consumers/', views.edit_consumer, name='edit_consumer'),

]