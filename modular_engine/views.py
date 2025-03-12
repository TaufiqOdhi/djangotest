from django.shortcuts import render
from .models import AppModule

# Create your views here.
def index(request):
    list_app_modules = AppModule.objects.filter(deleted_at=None)
    return render(
        request=request,
        template_name='./modular_engine/index.html',
        context= dict(list_app_modules=list_app_modules)
    )
