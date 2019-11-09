from django.http import JsonResponse
from .models import Product, Manufacture

def product_list(request):
    products = Product.objects.all()[:30]
    data = {"products":list(products.values("pk", "name", "description", "photo", "price","shipping_cost"))}
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"products" : {
            "name": product.name,
            "manufacture":product.manufacture.name,
            "description": product.description,
            "photo":product.photo.url,
            "price" :product.price,
        }}

        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code":404,
                "message": "product not found"
            }
        }, status=404)
    
    return response


# from django.views.generic.detail import DetailView
# from django.views.generic.list  import ListView
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = "products/product_detail.html"

# class ProductListView(ListView):
#     model = Product
#     template_name = "products/product_list.html"