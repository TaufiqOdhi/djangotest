from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect

def module_not_installed(request):
    return render(request, 'module_not_installed.html', status=403)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/'))
            return HttpResponseRedirect(next_url)
        else:
            # Return an 'invalid login' error message.
            return render(
                request=request, 
                template_name='login.html',
                context={'error': 'Invalid username or password'})
    else:
        next_url = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))
        return render(
            request=request,
            template_name='login.html',
            context={'next': next_url})

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))
