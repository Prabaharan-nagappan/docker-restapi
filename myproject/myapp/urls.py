# myapp/urls.py
from django.urls import path
from .views import ItemListCreateView, ItemDetailView, UserRegistration

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('register/', UserRegistration.as_view(), name='user-registration'),
]
