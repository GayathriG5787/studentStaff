from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
# from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello World")

class HomeView(TemplateView):
    template_name = 'accounts/home.html'
    
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return reverse_lazy('dashboard')

# User is class and user is object of that class
class DashboardRedirectView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.role == 'admin':
            return redirect('admin-dashboard')
        return redirect('student-dashboard')
    
