from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from Nemo.models import Room, Message
import random


# Create your views here.
def index(request):
    request.session['suffix'] = str(random.randint(100000,1000000))
    request.session['username'] = 'u/' + request.session['suffix']
    username = request.session['username']
    request.session['ipaddress'] = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
    return render(request, 'home.html', {'username':username,})

def home(request):
    rooms = Room.objects.all()
    username = request.session['username']
    
    if request.method == 'POST':
        room = Room(name = request.POST.get('room'))
        room.admin = request.session['ipaddress']
        room = room.save()
        message = 'Successfully created room'
        return render(request, 'develop.html', {'rooms':rooms, 'message' : message, 'username':username,})        
    else:
        return render(request, 'develop.html', {'rooms':rooms, 'username':username,})

def room(request, slug, id):
    username = request.session['username']    
    room = get_object_or_404(Room, id=id)
    all_messages = Message.objects.all().order_by('-id')
    messages = all_messages.filter(room=room)
    name = room.name.upper()
    if room.admin == request.session['ipaddress']:
        Admin = True
    else:
        Admin = False

    if request.method == 'POST':
        message = Message(message = request.POST.get('message'))
        message.poster = request.session['username']
        message.room = room
        message = message.save()
        return redirect('room', slug=room.slug, id=room.id)
    else:
        return render(request, 'room.html', {'room' : room, 'messages' : messages, 'username':username, 'admin' : Admin, 'name' : name,})