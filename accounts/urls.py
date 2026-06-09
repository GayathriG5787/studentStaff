from django.urls import path
from .views import HomeView, CustomLoginView, DashboardRedirectView

urlpatterns = [
    path('', HomeView.as_view(), name= "home"),
    path('login/', CustomLoginView.as_view(), name="login" ),
    path('dashboard/', DashboardRedirectView.as_view(), name="dashboard" ),
]