from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm, ItemForm
from .models import Room, Item

# Create your views here.
# For every function you create, you need to add it to the urls.py file
# dummy data 
class Room:
    def __init__(self, id, name):
        self.id = id
        self.name = name

rooms = [
    Room(1, 'Bedroom'),
    Room(2, 'Living Room'),
    Room(3, 'Kitchen'),
    Room(4, 'Bathroom'),
    Room(5, 'Garage')
]

class Item:
    def __init__(self, id, name, description, quantity, room):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.room = room

items = [
    Item(1, 'Hammer', 'A basic hammer', 1, rooms[4]),
    Item(2, 'Keys', 'House keys', 1, rooms[4]),
    Item(3, 'Screwdriver', 'Phillips head screwdriver', 1, rooms[4]),
    Item(4, 'Tape', 'Scotch tape', 2, rooms[2]),
    Item(5, 'Marker', 'Black permanent marker', 3, rooms[2])
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
    room = next((room for room in rooms if room.id == room_id), None)
    if room is None:
        return HttpResponse("Room not found", status=404)
    return render(request, 'rooms/show.html', {'room': room})

def rooms_edit(request, room_id):
    room = next((room for room in rooms if room.id == room_id), None)
    if room is None:
        return HttpResponse("Room not found", status=404)
    return render(request, 'rooms/edit.html', {'room': room})

def rooms_update(request, room_id):
    return HttpResponse("Room updated!")

def rooms_delete(request, room_id):
    return HttpResponse("Room deleted!")

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'registration/profile.html', {'form': form})

def items_index(request):
    return render(request, 'items/index.html', {'items': items})

def items_new(request):
    return render(request, 'items/new.html')

def items_create(request):
    return HttpResponse("Item created!")

def items_detail(request, item_id):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        return HttpResponse("Item not found", status=404)
    return render(request, 'items/show.html', {'item': item})

def items_edit(request, item_id):
    item = next((item for item in items if item.id == item_id), None)
    if item is None:
        return HttpResponse("Item not found", status=404)
    return render(request, 'items/edit.html', {'item': item})

def items_update(request, item_id):
    return HttpResponse("Item updated!")

def items_delete(request, item_id):
    return HttpResponse("Item deleted!")