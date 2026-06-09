from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView

# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello World")

class HomeView(TemplateView):
    template_name = 'accounts/home.html'
    
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

