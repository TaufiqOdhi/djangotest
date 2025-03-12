from django.contrib import admin
from .models import Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'barcode', 'price', 'stock']
    search_fields = ['name', 'barcode']
    list_filter = ['created_at', 'updated_at', 'deleted_at']

admin.site.register(Product, AdminProduct)
