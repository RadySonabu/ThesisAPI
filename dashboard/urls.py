from django.urls import path, include
from .views import dashboard, about_page
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('about/', about_page, name='about'),
    
]
