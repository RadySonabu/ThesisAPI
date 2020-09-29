from django.urls import path, include
from .views import (
    dashboard, 
    about_page, 
    home, 
    services,
    register,
    profile,
    )

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('about/', about_page, name='about'),
    path('services/', services, name='services'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    
]
