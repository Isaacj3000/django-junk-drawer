from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

def home(request):
    return render(request, 'landing.html')

# ✅ List all rooms for the logged-in user
@login_required
def rooms_index(request):
    rooms = Room.objects.filter(owner=request.user)
    return render(request, 'rooms/index.html', { 'rooms': rooms })

# ✅ Show detail page for a specific room
@login_required
def rooms_detail(request, room_id):
    room = get_object_or_404(Room, pk=room_id, owner=request.user)
    return render(request, 'rooms/show.html', { 'room': room })

# Show form to create a new room
@login_required
def rooms_new(request):
    form = RoomForm()
    return render(request, 'rooms/new.html', { 'form': form })

# Handle submission to create a new room
@login_required
def rooms_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            new_room = form.save(commit=False)
            new_room.owner = request.user
            new_room.save()
            return redirect('rooms_index')
    return redirect('rooms_new')

# Show form to edit an existing room
@login_required
def rooms_edit(request, room_id):
    room = get_object_or_404(Room, pk=room_id, owner=request.user)
    form = RoomForm(instance=room)
    return render(request, 'rooms/edit.html', { 'room': room, 'form': form })

# Handle submission to update room
@login_required
def rooms_update(request, room_id):
    room = get_object_or_404(Room, pk=room_id, owner=request.user)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms_detail', room_id=room.id)
    return redirect('rooms_edit', room_id=room.id)

# Handle room deletion
@login_required
def rooms_delete(request, room_id):
    room = get_object_or_404(Room, pk=room_id, owner=request.user)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms_index')
    return redirect('rooms_detail', room_id=room.id)
