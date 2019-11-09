from django.http import JsonResponse
from .models import Product, Manufacture

def product_list(request):
    products = Product.objects.all()[:30]
    data = {"products":list(products.values("pk", "name", "description", "photo", "price","shipping_cost"))}
    response = JsonResponse(data)
    return response

# from django.views.generic.detail import DetailView
# from django.views.generic.list  import ListView
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"