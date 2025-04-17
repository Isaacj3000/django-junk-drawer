from django.urls import path, include
from . import views

# This is the URL configuration for the junk_app.
# dont foget to add your URLs here for each view you create
urlpatterns = [
    path('', views.home, name='home'),
]