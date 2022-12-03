from django.shortcuts import render

def index(request):
    print('index views')
    return render(request, "socketapp/index.html")

def room(request, room_name):
    print('room views')
    return render(request, "socketapp/room.html", {"room_name": room_name})