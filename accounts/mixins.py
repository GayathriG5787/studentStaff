from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'admin'
    
    def handle_no_permission(self):
        messages.error(
            self.request, "Only admins can access this page"
        )
        
        if self.request.user.is_authenticated:
            return redirect('student-dashboard')
        
        return redirect('login')
        
    
class StudentRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'student'
    
    def handle_no_permission(self):
        messages.error(
            self.request, "Only students can access this page"
        )
        
        if self.request.user.is_authenticated:
            return redirect('admin-dashboard')
        
        return redirect('login')