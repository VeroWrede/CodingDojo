from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "answer" : 42
    }
    return render(request, "index.html", context)

def create(request):
    if request.method == "POST":
        Album.objects.create(title = request.POST['title'], artist = request.POST['artist'], year = request.POST['year'])
    # Simulating post response
    return redirect("/")

def edit(request, album_id):
    if request.method == "POST":
        a = Album.objects.get(id = album_id)
        #print(a.id)
        a.title = request.POST['title']
        a.artist = request.POST['artist']
        a.year = request.POST['year']
        a.save()
    return redirect("/")

def delete(request):
    if request.method == "POST":
        deleted_album = Album.objects.get(id = request.POST['id']).delete()
    return redirect("/")

#copied and pasted from edit()
def read(request, album_id):
    if request.method == "GET":
        context = { "Album" : Album.objects.get(id = album_id)}
    return render(request, "index.html", context)


