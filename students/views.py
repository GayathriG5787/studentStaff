from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, DetailView
from .forms import StudentCreateForm
from .models import Student
from accounts.models import User

from django.contrib import messages

from django.urls import reverse_lazy

from accounts.mixins import AdminRequiredMixin, StudentRequiredMixin

class AdminDashboard(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'students/admin_dashboard.html'
    
class StudentDashboard(LoginRequiredMixin, StudentRequiredMixin,TemplateView):
    template_name = 'students/student_dashboard.html'
    
class StudentCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Student
    form_class = StudentCreateForm
    
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('admin-dashboard')
    
    def form_valid(self, form):
        user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            role = 'student'
        )
        
        self.object = form.save(commit=False)
        self.object.user = user
        self.object.save()
        messages.success(self.request, "Student Profile has been created successfully")
        return super().form_valid(form)    
    
class StudentProfileView(LoginRequiredMixin, StudentRequiredMixin, DetailView):
    model = Student
    template_name = 'students/profile.html'
    # Gives name for object
    context_object_name = 'student'
    
    # get_object is a conventional function name
    def get_object(self):
        return Student.objects.get(
            user = self.request.user
        )
