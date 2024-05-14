from django.urls import path
from .views import product_list, featured_products

urlpatterns = [
    path('products/', product_list),
    path('products/featured/', featured_products),
]