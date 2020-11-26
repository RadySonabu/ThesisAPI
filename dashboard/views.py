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


def dashboard(request):
    url = f'https://document-dot-samp-051520.et.r.appspot.com/api/v1/file/list/?uploader={request.user}'
    user_url = f'http://thesis-web-app-dot-samp-051520.et.r.appspot.com/api/v1/user/retrieve/{request.user}'
    csv_file_path = 'static/HAM10000_metadata.csv'

    user_response = requests.get(user_url)
    user_result = user_response.json()
    age = user_result['age']

    csv_file = pd.read_csv(csv_file_path)
    csv_file.isnull().sum()

    modified_csv_file = csv_file.dropna()
    modified_csv_file.isnull().sum()

    count = 0
    gender_list = []
    area_list = []
    for item in modified_csv_file.itertuples():

        if int(item[5]) > age - 3 and int(item[5]) < age + 3:
            count +=1
            gender_list.append(item[6])
            area_list.append(item[7])

    percent = area_list.count('upper extremity')/count
    gender_female = gender_list.count('female')
    gender_male = gender_list.count('male')
    total_gender = gender_female + gender_male
    gender_cancer = f'At age {age-5} - {age+10}, female with skin cancer is/are approximately{gender_female} and male with skin cancer is/are approximately {gender_male}'
    face =area_list.count('face')
    upper_extremity = area_list.count('upper extremity')
    print(round(percent*100, 2))
    print(count)





    context = {
        'gender_cancer': gender_cancer,
        'gender_male': gender_male,
        'gender_female': gender_female,
        'total_gender': total_gender,
        'face': face,
        'upper_extremity': upper_extremity,
    }
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
    
    list_of_uploads = []
    for item in r.json()['results']:
        list_of_uploads.append(item)
        print(item)

    url = f'https://document-dot-samp-051520.et.r.appspot.com/api/v1/file/list/?uploader={request.user}'
    user_url = f'http://thesis-web-app-dot-samp-051520.et.r.appspot.com/api/v1/user/retrieve/{request.user}'
    csv_file_path = 'static/HAM10000_metadata.csv'

    user_response = requests.get(user_url)
    user_result = user_response.json()
    print(user_result)
    age = user_result['age']

    csv_file = pd.read_csv(csv_file_path)
    csv_file.isnull().sum()

    modified_csv_file = csv_file.dropna()
    modified_csv_file.isnull().sum()

    count = 0
    gender_list = []
    area_list = []
    for item in modified_csv_file.itertuples():

        if int(item[5]) > age - 3 and int(item[5]) < age + 3:
            count +=1
            gender_list.append(item[6])
            area_list.append(item[7])

    percent = area_list.count('upper extremity')/count
    gender_female = gender_list.count('female')
    gender_male = gender_list.count('male')
    total_gender = gender_female + gender_male
    gender_cancer = f'At age {age-5} - {age+10}, female with skin cancer is/are approximately {gender_female} and male with skin cancer is/are approximately {gender_male}'
    abdomen =area_list.count('abdomen')
    acral =area_list.count('acral')
    back =area_list.count('back')
    chest =area_list.count('chest')
    ear =area_list.count('ear')
    face =area_list.count('face')
    foot =area_list.count('foot')
    genital =area_list.count('genital')
    hand =area_list.count('hand')
    lower_extremity =area_list.count('lower extremity')
    neck =area_list.count('neck')
    scalp =area_list.count('scalp')
    trunk =area_list.count('trunk')
    unknown =area_list.count('unknown')
    upper_extremity = area_list.count('upper extremity')
    # abdomen, acral, back, chest, ear, face, foot, genital, hand, lower extremity, neck, scalp, trunk, uknown, upper extremity
    context = {
        'gender_cancer': gender_cancer,
        'gender_male': gender_male,
        'gender_female': gender_female,
        'total_gender': total_gender,
        'abdomen':abdomen,
        'acral':acral,
        'back':back,
        'chest':chest,
        'ear':ear,
        'face':face,
        'foot':foot,
        'genital':genital,
        'hand':hand,
        'lower_extremity':lower_extremity,
        'neck':neck,
        'scalp':scalp,
        'trunk':trunk,
        'unknown':unknown,
        'upper_extremity':upper_extremity,
        'uploads': list_of_uploads,
    }
    return render(request, 'dashboard/home.html', context)

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
            return redirect('home')
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

def analytics(request):
    context = {
        'analytics': 'this is analytics'
    }
    return render(request, 'dashboard/landing_page.html', context)




