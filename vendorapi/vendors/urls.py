from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateDestroyView, OnboardedVendorListView
from .views import  UserSignupView, UserLoginView

# Define your URL patterns here
urlpatterns = [
    path('registered-vendors/', VendorListCreateView.as_view(), name='registered-vendors'),
    path('onboarded-vendors/', OnboardedVendorListView.as_view(), name="onboarded-vendors"),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-detail'),
    path('vendors/signup/', UserSignupView.as_view(), name='vendor-signup'),
    path('vendors/login/', UserLoginView.as_view(), name='vendor-login'),
]