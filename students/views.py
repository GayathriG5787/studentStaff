from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.mixins import AdminRequiredMixin, StudentRequiredMixin

class AdminDashboard(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'students/admin_dashboard.html'
    
class StudentDashboard(LoginRequiredMixin, StudentRequiredMixin ,TemplateView):
    template_name = 'students/student_dashboard.html'
