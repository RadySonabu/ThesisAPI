from django.urls import path, include
from .views import dashboard, about_page, home, services
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('about/', about_page, name='about'),
    path('services/', services, name='services'),
    
]
