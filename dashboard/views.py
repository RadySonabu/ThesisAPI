from django.shortcuts import render, redirect
from user.models import MyUser
from user.forms.forms import UserRegisterForm

def dashboard(request):
    context = {}
    return render(request, 'dashboard/landing_page.html', context)

def about_page(request):
    context = {}
    return render(request, 'dashboard/about.html', context)

def home(request):
    context = {}
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