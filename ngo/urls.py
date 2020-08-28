from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('admin-profile/', views.admin_profile, name='admin_profile'),
    path('request-donation/', views.request_donation, name='request_donation'),
    path('donation/<int:id>/request-approve/', views.approve_request, name='approve_request'),
    path('request/<int:id>/donate/', views.make_donation, name='donate'),
    path('request/<int:pk>/', views.DonationDetailView.as_view(), name='donation-detail'),
    path('request/<int:pk>/update/', views.DonationUpdateView.as_view(), name='update-donation'),
    path('request/<int:pk>/delete/', views.DonationDeleteView.as_view(), name='delete-donation'),

    # path('request/<int:id>/', views.donations_detail, name='donation-detail'),

]