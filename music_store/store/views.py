from django.shortcuts import render
from .models import Artist, Album

def home(request):
    return render(request, 'store/home.html')

def artist_list(request):
    artists = Artist.objects.all().order_by('debut_year')

    context = {
        'artists': artists
    }
    return render(request, 'store/artist_list.html', context)

def album_list(request):
    albums = Album.objects.all().order_by('release_date')

    context = {
        'albums': albums
    }
    return render(request, 'store/album_list.html', context)

