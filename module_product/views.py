from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    list_products = Product.objects.filter(deleted_at=None)
    return render(
        request=request,
        template_name='module_product/index.html',  # Updated path
        context=dict(list_products=list_products)
    )

