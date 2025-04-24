from django import forms
from .models import Room, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }