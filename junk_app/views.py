from django.shortcuts import render
from django.http import HttpResponse


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
    return HttpResponse("migrations worked! Server is running");


