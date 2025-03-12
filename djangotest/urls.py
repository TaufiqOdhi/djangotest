"""
URL configuration for djangotest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from .views import module_not_installed, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('module', include('modular_engine.urls'), name='modular_engine'),
    path('module/product', include('module_product.urls'), name='module_product'),
    path('module_not_installed/', module_not_installed, name='module_not_installed'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', lambda request: HttpResponseRedirect('/module')),  # Redirect root URL to /module
]
