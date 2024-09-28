from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout

class login(TemplateView):
    template_name = 'login.html'

def logout(request):
    # ...
    auth_logout(request)
    return redirect('/')
