from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm

# Create your views here.
# For every function you create, you need to add it to the urls.py file
# dummy data 
class Room:
    def __init__(self, name):
        self.name = name,

rooms = [
    Room('Bedroom'),
    Room('Living Room'),
    Room('Kitchen'),
    Room('Bathroom'),
    Room('Garage')
]

class Item:
    def __init__(self, name, room, isCorrectRoom):
        self.name = name,
        self.room = room,
        self.isCorrectRoom = isCorrectRoom,

items = [
    Item('Hammer', 'Garage', False),
    Item('Keys', 'Garage', True),
    Item('Screwdriver', 'Garage', False),
    Item('Tape', 'Kitchen', True),
    Item('Marker', 'Kitchen', False),
]

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        form = AuthenticationForm()
        return render(request, 'home.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})

def rooms_index(request):
    return render(request, 'rooms/index.html', {'rooms': rooms})

def rooms_new(request):
    return render(request, 'rooms/new.html')

def rooms_create(request):
    return HttpResponse("Room created!")

def rooms_detail(request, room_id):
    return render(request, 'rooms/show.html', {'room': rooms[room_id - 1]})

def rooms_edit(request, room_id):
    return render(request, 'rooms/edit.html', {'room': rooms[room_id - 1]})

def rooms_update(request, room_id):
    return HttpResponse("Room updated!")

def rooms_delete(request, room_id):
    return HttpResponse("Room deleted!")

@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'registration/profile.html', {'form': form})