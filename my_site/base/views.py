from django.shortcuts import render, redirect
from .models import SoundClip
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Fridays With Pewdiepie'},
    {'id': 2, 'name': 'I love memes'},
    {'id': 3, 'name': 'Cor yeah mate'},
]

def home(request):
    return redirect('soundboard')

def soundboard(request):
    sounds = SoundClip.objects.all()
    context = {
        'rooms': rooms,
        'sounds': sounds,
        }
    return render(request, 'base/home.html', context)

def individual_clip(request, pk):
    sound = SoundClip.objects.get(id=pk)
    context = {'sound': sound}
    return render(request, 'base/clip_card.html', context)

def test(request):
    return HttpResponse("Test")