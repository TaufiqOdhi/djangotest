from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from .models import Product

# Create your views here.
class IndexView(View):
    def get(self, request):
        list_products = Product.objects.filter(deleted_at=None)
        return render(
            request=request,
            template_name='module_product/index.html',
            context=dict(list_products=list_products)
        )
    
    def post(self, request):
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')

        if action == 'create':
            self.create(post_data=request.POST)
        elif action == 'update':
            self.update(post_data=request.POST, product_id=product_id)
        elif action == 'delete':
            self.delete(product_id=product_id)
        
        return redirect('module_product')
    
    def create(self, post_data):
        Product.objects.create(
            name=post_data.get('name'),
            barcode=post_data.get('barcode'),
            price=post_data.get('price'),
            stock=post_data.get('stock')
        )

    def update(self, post_data, product_id: int):
        product = Product.objects.get(id=product_id)
        product.name = post_data.get('name')
        product.barcode = post_data.get('barcode')
        product.price = post_data.get('price')
        product.stock = post_data.get('stock')  
        product.save()    
    
    def delete(self, product_id: int):
        product = Product.objects.get(id=product_id)
        product.deleted_at = datetime.now()
        product.save()
