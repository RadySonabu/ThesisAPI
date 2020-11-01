from django.shortcuts import render, redirect
from user.models import MyUser
from user.forms.forms import UserRegisterForm
from .forms import FileUploadForm
import requests
from django.conf import settings


def dashboard(request):
    context = {}
    return render(request, 'dashboard/landing_page.html', context)

def about_page(request):
    context = {}
    return render(request, 'dashboard/about.html', context)

def home(request):
    uploader = str(request.user)
    headers = {
        'Content-type': 'application/json'
    }
    r = requests.get(f'https://document-dot-samp-051520.et.r.appspot.com/api/v1/file/list/?uploader={uploader}', headers=headers)
    
    print(r.json())
    list_of_uploads = []
    for item in r.json()['results']:
        list_of_uploads.append(item)
        print(item)

    doctors = MyUser.objects.filter(role=1)
    print(f'doctor: {doctors}')
    context = {
        'uploads': list_of_uploads,
        'doctors': doctors
    }
    return render(request, 'dashboard/home.html', context)

def services(request):
    context = {}
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


def profile(request):
    context = {}
    return render(request, 'dashboard/profile.html', context)


def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            
            file_upload = form.cleaned_data.get('file_upload')
            body = {
                        "uploader": f'{request.user}',
                }
            files = {"file_uploaded": file_upload}
            headers = {
                "Content-Type": "multipart/form-data"
            }
            r = requests.post('https://document-dot-samp-051520.et.r.appspot.com/api/v1/file/create/', data=body,  files=files)
            print(r)
            # print(r.json())
            # messages.success(request, f'Account created for {student_number}!')
            return redirect('services')
    else:
        form = FileUploadForm()

    context = { 
        # 'r': r.json(),
        'form': form  }
    return render(request, 'dashboard/file_upload/file_upload_page.html', context)

def video_chat(request, slug, *args, **kwargs):


    slug = request.user.id
    room_api_link = f'https://thesis-video-chat-dot-samp-051520.et.r.appspot.com/api/v1/room/?search={slug}'

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

def create_room(request):

    room_api_link = 'https://thesis-video-chat-dot-samp-051520.et.r.appspot.com/api/v1/room/'
    
    payload = {
        'title': str(request.user.id),
        'status': 'Active'
    }

    r = requests.post(room_api_link, data=payload)
    return redirect('video-chat', slug=str(request.user.id))


def view_contact_information(request, id, *args, **kwargs):
    doctor = MyUser.objects.filter(role=1).get(id=id)

    context={
        'doctor': doctor,
    }
    return render(request, 'dashboard/contact.html', context)



