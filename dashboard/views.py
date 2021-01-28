from django.shortcuts import render, redirect
from user.models import MyUser
from user.forms.forms import UserRegisterForm
from .forms import FileUploadForm
import requests
import pandas as pd
import io
import matplotlib.pyplot as plt
import urllib, base64
from django.conf import settings
from app.constants import DOCUMENT_API_URL, VIDEO_API_URL, USER_API_URL
from django.contrib.auth.decorators import login_required

def dashboard(request):
    url = f'{DOCUMENT_API_URL}/api/v1/file/list/?uploader={request.user}'
    user_url = f'{USER_API_URL}/api/v1/user/retrieve/{request.user}'
    r = requests.get(url)
    print(r.json())
    





    context = {
        
    }
    return render(request, 'dashboard/landing_page.html', context)

def about_page(request):
    context = {}
    return render(request, 'dashboard/about.html', context)

@login_required
def home(request):
    uploader = str(request.user)
    headers = {
        'Content-type': 'application/json'
    }
    # try:
    try:
        r = requests.get(f'{DOCUMENT_API_URL}/api/v1/file/list/?uploader={uploader}', headers=headers)
        r2 = requests.get(f'{DOCUMENT_API_URL}/api/v1/file/get-analytics/')
        analytics = r2.json()
        list_of_uploads = r.json()[0]
    except:
        list_of_uploads = {}
    context = {
        'uploads': list_of_uploads,
        'analytics': analytics
    }
    # except:
    #     redirect('login')
    #     context = {}
    return render(request, 'dashboard/home.html', context)

@login_required
def available_doctor(request):
    doctors = MyUser.objects.filter(role=1)
    context = {
        'doctors': doctors,
    }
    return render(request, 'dashboard/services.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            # messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'dashboard/registration.html', {'form': form})

@login_required
def profile(request):
    context = {}
    return render(request, 'dashboard/profile.html', context)

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            
            file_upload = form.cleaned_data.get('file_upload')
            patient_name = form.cleaned_data.get('patient_name')
            patient_gender = form.cleaned_data.get('patient_gender')
            patient_age = form.cleaned_data.get('patient_age')
            lesion_location = form.cleaned_data.get('lesion_location')
            body = {
                        "uploader": f'{request.user}',
                        "patient_name": patient_name,
                        "patient_gender": patient_gender,
                        "patient_age": patient_age,
                        "lesion_location": lesion_location,
                }
            files = {"file_uploaded": file_upload}
            headers = {
                "Content-Type": "multipart/form-data"
            }
            r = requests.post(f'{DOCUMENT_API_URL}/api/v1/file/create/', data=body,  files=files)
            return redirect('home')
    else:
        form = FileUploadForm()

    context = { 
        'form': form  }
    return render(request, 'dashboard/file_upload/file_upload_page.html', context)

@login_required
def video_chat(request, slug, *args, **kwargs):


    slug = request.user.id
    room_api_link = f'{VIDEO_API_URL}/api/v1/room/?search={slug}'

    r = requests.get(room_api_link)
    room = r.json()[0]
    print(r)
    print(r.json())

    context = {
        'apiKey':settings.TOK_KEY, 
        'session':room['session'], 
        'token':room['token'], 
        'slug': room['slug'],
    }

    return render(request, 'dashboard/video_chat/video_chat.html', context)

@login_required
def create_room(request):

    room_api_link = f'{VIDEO_API_URL}/api/v1/room/'
    
    payload = {
        'title': str(request.user.id),
        'status': 'Active'
    }

    r = requests.post(room_api_link, data=payload)
    print(r)
    return redirect('video-chat', slug=str(request.user.id))


def view_contact_information(request, id, *args, **kwargs):
    doctor = MyUser.objects.filter(role=1).get(id=id)

    context={
        'doctor': doctor,
    }
    return render(request, 'dashboard/contact.html', context)

@login_required
def analytics(request):
    r2 = requests.get(f'{DOCUMENT_API_URL}/api/v1/file/get-analytics/')
    analytics = r2.json()
    context = {
        'analytics': analytics
    }
    return render(request, 'dashboard/analytics.html', context)

def terms_and_conditions(request):
    context = {}
    return render(request, 'dashboard/terms_and_conditions.html', context)


