from django.urls import path, include
from .views import (
    dashboard, 
    about_page, 
    home, 
    available_doctor,
    register,
    profile,
    file_upload,
    video_chat, 
    create_room,
    view_contact_information,
    analytics,
    )
from user.views import update_user, delete_user
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home, name='home'),
    path('about/', about_page, name='about'),
    path('doctors/', available_doctor, name='available-doctor'),
    path('upload/', file_upload, name='file-upload'),
    path('register/', register, name='register'),
    path('profile/update/', update_user, name='profile-update'),
    path('profile/delete/<id>/', delete_user, name='profile-delete'),
    path('profile/', profile, name='profile'),
    path('video-chat/<slug>/', video_chat, name='video-chat'),
    path('create-room/', create_room, name='create-room'),
    path('contact-info/<id>/', view_contact_information, name='contact-info'),
    path('analytics/', analytics, name='analytics'),
    
]
