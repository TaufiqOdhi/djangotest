from django.contrib import admin
from .models import AppModule

# Register your models here.
class AdminAppModule(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_installed', 'created_at', 'updated_at', 'deleted_at']
    search_fields = ['name']
    list_filter = ['is_installed', 'created_at', 'updated_at', 'deleted_at']

admin.site.register(AppModule, AdminAppModule)
