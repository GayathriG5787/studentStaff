from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello World")

class HomeView(TemplateView):
    template_name = 'accounts/home.html'
    
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class DashboardRedirectView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.role == 'admin':
            return redirect('admin-dashboard')
        return redirect('student-dashboard')
    
    
# I meant student