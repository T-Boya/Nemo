from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect, HttpResponse
from Nemo.models import Room, Message

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        room = Room(name = request.POST.get('room'))
        room = room.save()
        message = 'Successfully created room'
        return render(request, 'develop.html', {'rooms':rooms, 'message' : message,})        
    else:
        return render(request, 'develop.html', {'rooms':rooms,})

def room(request, slug, id):
    room = get_object_or_404(Room, id=id)
    all_messages = Message.objects.all().order_by('-id')
    messages = all_messages.filter(room=room)
    if request.method == 'POST':
        message = Message(message = request.POST.get('message'))
        message.poster = 'Joe'
        message.room = room
        message = message.save()
        return redirect('room', slug=room.slug, id=room.id)
    else:
        return render(request, 'room.html', {'room' : room, 'messages' : messages,})