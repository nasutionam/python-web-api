from django.urls import path
from .views import product_list, product_detail, manufacture_list, manufacture_detail

urlpatterns = [
    path("products/",product_list, name='product-list'),
    path("products/<int:pk>/", product_detail, name='product-detail'),
    path("manufactures/", manufacture_list, name='manufacture-list'),
    path("manufactures/<int:pk>/", manufacture_detail, name='manufacture-detail'),
    
]