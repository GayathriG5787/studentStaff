from django.urls import path
from .views import AdminDashboard, StudentDashboard, StudentCreateView, StudentProfileView

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin-dashboard/', AdminDashboard.as_view(), name='admin-dashboard'),
    path('student-dashboard/', StudentDashboard.as_view(), name='student-dashboard'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('students/add/', StudentCreateView.as_view(), name='student-add'),
    path('student/profile', StudentProfileView.as_view(), name= 'student-profile')
]