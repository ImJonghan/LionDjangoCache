from django.http import JsonResponse
from django.core.cache import cache
from .models import Product
from django.core.serializers import serialize

def product_list(request):
    cache_key = 'full_product_list'
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)
    products = list(Product.objects.all().values('id', 'name', 'price', 'is_featured'))
    cache.set(cache_key, products, timeout=3600)
    return JsonResponse(products, safe=False)

def featured_products(request):
    cache_key = 'featured_product_list'
    cached_data = cache.get(cache_key)
    if cached_data:
        return JsonResponse(cached_data, safe=False)
    products = list(Product.objects.filter(is_featured=True).values('id', 'name', 'price'))
    cache.set(cache_key, products, timeout=3600)
    return JsonResponse(products, safe=False)