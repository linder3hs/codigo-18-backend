from django.urls import path
from .views import get_products

urlpatterns = [
    path('products/', get_products, name='products_list')
]
