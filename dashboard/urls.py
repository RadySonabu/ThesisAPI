from django.urls import path, include
from .views import (
    dashboard, 
    about_page, 
    home, 
    services,
    register,
    profile,
    file_upload,
    video_chat, 
    create_room,
    view_contact_information,
    )

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('about/', about_page, name='about'),
    path('services/', services, name='services'),
    path('upload/', file_upload, name='file-upload'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('video-chat/<slug>/', video_chat, name='video-chat'),
    path('create-room/', create_room, name='create-room'),
    path('contact-info/<id>/', view_contact_information, name='contact-info'),
    
]
