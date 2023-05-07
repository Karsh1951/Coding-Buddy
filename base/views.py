from django.shortcuts import render,redirect
from .models import Room, Topic
from .forms import  RoomForm

# Create your views here
# 

#rooms = [
 #   {'id': 1, 'name': 'lets learn python'},
 #{'id': 2, 'name': 'Design with me '},         
 #{'id': 3, 'name': 'frontend developers'},
#] 
def home(request):
    rooms = Room.objects.all()
    topics =Topic.objects.all()
    context = {'rooms': rooms,'topics': topics}
    return render(request, 'base/home.html', context)

#passing in another parameter to access value in url
def room(request, pk):
   #setting value for room and looping through it,value is none
    room= Room.object.get(id=pk)
    context={'room': room}  
        
    return render(request,'base/room.html',context)
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
            
    context={'form': form}
    return render(request,'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk) 
    form= RoomForm(initial=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form} 
    
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html', {'obj':room})    



      