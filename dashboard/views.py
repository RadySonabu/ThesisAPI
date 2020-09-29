from django.shortcuts import render

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