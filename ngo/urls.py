from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('admin-profile', views.admin_profile, name='admin_profile'),
    path('request-donation/', views.request_donation, name='request_donation'),
    path('donation/<int:id>/request-approve/', views.approve_request, name='approve_request')
]