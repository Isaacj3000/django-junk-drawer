from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm, ItemForm
from .models import Room, Item, UserProfile


@login_required
def home(request):
    return render(request, 'home.html')

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

@login_required
def rooms_index(request):
    rooms = Room.objects.filter(user=request.user)
    return render(request, 'rooms/index.html', {'rooms': rooms})

@login_required
def rooms_new(request):
    return render(request, 'rooms/new.html')

@login_required
def rooms_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        room = Room.objects.create(name=name, user=request.user)
        return redirect('rooms_detail', room_id=room.id)
    return redirect('rooms_index')

@login_required
def rooms_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    return render(request, 'rooms/show.html', {'room': room})

@login_required
def rooms_edit(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    return render(request, 'rooms/edit.html', {'room': room})

@login_required
def rooms_update(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    if request.method == 'POST':
        room.name = request.POST.get('name')
        room.save()
        return redirect('rooms_detail', room_id=room.id)
    return redirect('rooms_index')

@login_required
def rooms_delete(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms_index')
    return redirect('rooms_index')

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

@login_required
def items_index(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'items/index.html', {'items': items})

@login_required
def items_new(request):
    return render(request, 'items/new.html')

@login_required
def items_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('items_detail', item_id=item.id)
    return redirect('items_index')

@login_required
def items_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    return render(request, 'items/show.html', {'item': item})

@login_required
def items_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    return render(request, 'items/edit.html', {'item': item})

@login_required
def items_update(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('items_detail', item_id=item.id)
    return redirect('items_index')

@login_required
def items_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('items_index')
    return redirect('items_index')







