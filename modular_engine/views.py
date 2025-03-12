from django.shortcuts import render, redirect
from django.views import View
from django.core.management import call_command
from .models import AppModule

# Create your views here.
class IndexView(View):
    def get(self, request):
        list_app_modules = AppModule.objects.filter(deleted_at=None)
        return render(
            request=request,
            template_name='modular_engine/index.html',  # Updated path
            context=dict(list_app_modules=list_app_modules)
        )
    
    def post(self, request):
        app_module_id = request.POST.get('app_module_id')
        action = request.POST.get('action')
        app_module = AppModule.objects.get(id=app_module_id)
        
        if action == 'install':
            self.install(app_module)
        elif action == 'uninstall':
            self.uninstall(app_module)
        elif action == 'upgrade':
            self.upgrade(app_module)
        
        return redirect('modular_engine')
    
    def install(self, app_module: AppModule):
        app_module.is_installed = True
        app_module.save()
    
    def uninstall(self, app_module: AppModule):
        app_module.is_installed = False
        app_module.save()

    def upgrade(self, app_module: AppModule):
        app_name = f'module_{app_module.name}'
        call_command('makemigrations', app_name)
        call_command('migrate', app_name)
