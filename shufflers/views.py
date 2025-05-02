from django.shortcuts import render
from django.http import HttpResponse
from main import main
from shufflers.forms import SongForm

# Create your views here.

def index(request):
    return render(request, 'shufflers/home.html')

def shufflesongs(request):
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            songs = form.cleaned_data['numSongs']
            main(songs)
    
    return render(request, 'shufflers/home.html')