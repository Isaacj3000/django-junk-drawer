from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Item
from .forms import RoomForm, ItemForm

# ---------- General Pages ----------

def landing(request):
    return render(request, 'landing.html')

@login_required
def home(request):
    return render(request, 'home.html')

# ---------- Room Views ----------

@login_required
def rooms_index(request):
    rooms = Room.objects.filter(user=request.user)
    return render(request, 'rooms/index.html', {'rooms': rooms})

@login_required
def rooms_new(request):
    form = RoomForm()
    return render(request, 'rooms/new.html', {'form': form})

@login_required
def rooms_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.user = request.user
            room.save()
            return redirect('rooms_index')
    return render(request, 'rooms/new.html', {'form': form})

@login_required
def rooms_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    return render(request, 'rooms/show.html', {'room': room})

@login_required
def rooms_edit(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    form = RoomForm(instance=room)
    return render(request, 'rooms/edit.html', {'form': form, 'room': room})

@login_required
def rooms_update(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('rooms_detail', room_id=room.id)
    return render(request, 'rooms/edit.html', {'form': form, 'room': room})

@login_required
def rooms_delete(request, room_id):
    room = get_object_or_404(Room, id=room_id, user=request.user)
    if request.method == 'POST':
        room.delete()
        return redirect('rooms_index')
    return redirect('rooms_detail', room_id=room.id)



@login_required
def items_index(request):
    items = Item.objects.filter(user=request.user)
    return render(request, 'items/index.html', {'items': items})

@login_required
def items_new(request):
    form = ItemForm(user=request.user)
    return render(request, 'items/new.html', {'form': form})

@login_required
def items_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, user=request.user)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('items_index')
    return render(request, 'items/new.html', {'form': form})

@login_required
def items_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    return render(request, 'items/show.html', {'item': item})

@login_required
def items_edit(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    form = ItemForm(instance=item, user=request.user)
    return render(request, 'items/edit.html', {'form': form, 'item': item})

@login_required
def items_update(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('items_detail', item_id=item.id)
    return render(request, 'items/edit.html', {'form': form, 'item': item})

@login_required
def items_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id, user=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('items_index')
    return redirect('items_detail', item_id=item.id)