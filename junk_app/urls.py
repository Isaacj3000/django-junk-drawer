from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.rooms_index, name='rooms_index'),
    path('rooms/new/', views.rooms_new, name='rooms_new'),
    path('rooms/create/', views.rooms_create, name='rooms_create'),
    path('rooms/<int:room_id>/', views.rooms_detail, name='rooms_detail'),
    path('rooms/<int:room_id>/edit/', views.rooms_edit, name='rooms_edit'),
    path('rooms/<int:room_id>/update/', views.rooms_update, name='rooms_update'),
    path('rooms/<int:room_id>/delete/', views.rooms_delete, name='rooms_delete'),
]