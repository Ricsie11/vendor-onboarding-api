from django.urls import path
from .views import VendorListCreateView, VendorRetrieveUpdateDestroyView

# Define your URL patterns here
urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-detail'),
]