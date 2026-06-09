from django.shortcuts import render
from django.views.generic import TemplateView

class AdminDashboard(TemplateView):
    template_name = 'students/admin_dashboard.html'
    
class StudentDashboard(TemplateView):
    template_name = 'students/student_dashboard.html'
