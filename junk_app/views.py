from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# For every function you create, you need to add it to the urls.py file
def home(request):
    return HttpResponse("migrations worked! Server is running");
