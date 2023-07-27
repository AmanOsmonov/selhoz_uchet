from django.urls import path
from .views import FarmerListView

urlpatterns = [
    path('api/farmers/', FarmerListView.as_view(), name='farmer-list'),
]