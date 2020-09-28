from django.shortcuts import render

def dashboard(request):
    context = {}
    return render(request, 'dashboard/landing_page.html', context=context)

def about_page(request):
    context = {}
    return render(request, 'dashboard/about.html', context=context)