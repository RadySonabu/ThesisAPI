from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import MyUser

class UserRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ['email', 
        'first_name', 'middle_name', 'last_name',
        'age', 'blood_type', 'role', 'phone_number',
        'street', 'city', 'barangay', 'postal_code'
        ]
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user