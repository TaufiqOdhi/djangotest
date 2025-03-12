from django.shortcuts import redirect
from .models import AppModule

class ModuleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if 'module/' is in the request path
        if 'module/' in request.path:
            # Get the module name from the request path
            module_name = request.path.split('module/')[1]
            
            try:
                app_module = AppModule.objects.get(name=module_name)
                if not app_module.is_installed:
                    return redirect('not_installed')  # Redirect to a "not installed" page
            except AppModule.DoesNotExist:
                pass  # If the module does not exist, continue as normal

        response = self.get_response(request)
        return response
