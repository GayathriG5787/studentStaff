from django.urls import path
from .views import AdminDashboard, StudentDashboard

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin-dashboard/', AdminDashboard.as_view(), name='admin-dashboard'),
    path('student-dashboard/', StudentDashboard.as_view(), name='student-dashboard'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout')
]