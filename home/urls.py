from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('file-case/', views.file_case, name='file_case'),
    path('emergency-services/', views.emergency_services, name='emergency_services'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
]
