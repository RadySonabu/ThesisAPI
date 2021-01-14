from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics

from .models import MyUser
from .forms.forms import UserRegisterForm, UpdateUserForm

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
    return render(request, 'user/registration.html', {'form': form})


def update_user(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')

    else:
        u_form = UpdateUserForm(instance=request.user)

    context = {
        'form': u_form,
    }

    return render(request, 'dashboard/profile-update.html', context)


def delete_user(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(MyUser, id = id) 
  
  
    if request.method =="POST": 
        # delete object 
        obj.delete() 
        # after deleting redirect to  
        # home page 
        return redirect("login") 
  
    return render(request, "dashboard/delete_user.html", context) 


def profile(request):
    context = {}
    return render(request, 'user/profile.html', context)