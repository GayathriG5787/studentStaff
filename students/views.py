from django.shortcuts import render
from django.views.generic import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin

class AdminDashboard(TemplateView):
    template_name = 'students/admin_dashboard.html'
    
class StudentDashboard(TemplateView):
    template_name = 'students/student_dashboard.html'
