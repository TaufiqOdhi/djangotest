from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View
from djangotest.utils import check_level_user
from .models import Product
from .forms import ProductForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(
            request=request,
            template_name='module_product/index.html',
            context=dict(
                list_products=Product.objects.filter(deleted_at=None),
                form=ProductForm(),
                level_user=check_level_user(user=request.user)
            )
        )
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')

        product_id = request.POST.get('product_id')
        form_data = ProductForm(request.POST)
        action = request.POST.get('action')
        level_user = check_level_user(user=request.user)

        if action == 'create':
            self.create(form_data=form_data, level_user=level_user)
        elif action == 'update':
            self.update(form_data=form_data, product_id=product_id, level_user=level_user)
        elif action == 'delete':
            self.delete(product_id=product_id, level_user=level_user)
        
        return redirect('module_product')
    
    def create(self, form_data: ProductForm, level_user: str):
        allowed_level_user = ['superuser', 'manager', 'user']
        if level_user in allowed_level_user:
            if form_data.is_valid():
                Product.objects.create(**form_data.cleaned_data)

    def update(self, form_data: ProductForm, product_id: int, level_user: str):
        allowed_level_user = ['superuser', 'manager', 'user']
        if level_user in allowed_level_user:
            if form_data.is_valid():
                Product.objects.filter(id=product_id).update(**form_data.cleaned_data)
    
    def delete(self, product_id: int, level_user: str):
        allowed_level_user = ['superuser', 'manager']
        if level_user in allowed_level_user:
            product = Product.objects.get(id=product_id)
            product.deleted_at = datetime.now()
            product.save()
