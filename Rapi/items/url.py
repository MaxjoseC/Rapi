from django.urls import path
from .views import ListCreateView, ItemDetailView

urlpatterns = [
    path('items/', ListCreateView.as_view(), name='item-list'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
]