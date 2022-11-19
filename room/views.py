from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message
from django.contrib import messages
# Create your views here.


@login_required
def rooms(request):
    """Create room and all Rooms send user."""
    if request.method == "POST":
        roomname = request.POST.get('roomname')
        slugroom = roomname.lower()
        print(roomname, slugroom)
        if slugroom:
            room = Room.objects.create(name=roomname, slug=slugroom)
            room.save()
            messages.success(request, f"{roomname} room create.")
        else:
            messages.error(request, f"Room name Empty")
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})


@login_required
def room(request, slug):
    """user ender room slug and this view room all message and user send many message of room."""
    room = Room.objects.get(slug=slug)
    messagess = Message.objects.filter(room=room)

    return render(request, 'room/room.html', {'room': room, "messagess": messagess})

