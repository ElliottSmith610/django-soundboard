from django.shortcuts import render, redirect
from .models import SoundClip, Message
from .forms import MessageForm, SoundclipForm
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
    form = SoundclipForm()
    context = {
        'rooms': rooms,
        'sounds': sounds,
        'form': form,
        }
    return render(request, 'base/home.html', context)

def individual_clip(request, pk):
    sound = SoundClip.objects.get(id=pk)
    comments = None #Message.objects.filter(sound)
    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        # TODO: Make the soundclip value, the current soundclip, and the user as current user
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('home')

    context = {'sound': sound, 'comments': comments, 'form': form}
    return render(request, 'base/clip_card.html', context)

def test(request):
    return HttpResponse("Test")