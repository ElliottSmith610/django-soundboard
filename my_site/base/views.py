from django.shortcuts import render, redirect
from .models import SoundClip, Message, Person
from .forms import MessageForm, SoundclipForm
from django.http import HttpResponse


def home(request):
    return redirect('soundboard')

def soundboard(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    sounds = SoundClip.objects.filter(person__name__icontains=q)
    person = Person.objects.all()

    context = {
        'sounds': sounds,
        'people': person,
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
            return redirect('home') # TODO: reload page with comments

    context = {
        'sound': sound,
        'comments': comments,
        'form': form
        }
    return render(request, 'base/clip_card.html', context)

def editClip(request, pk):
    soundclip = SoundClip.objects.get(id=pk)
    form = SoundclipForm(instance=soundclip)

    if request.method == 'POST':
        form = SoundclipForm(request.POST, instance=soundclip)
        if form.is_valid():
            form.save()
            return redirect('individual_clip', pk=soundclip.id)
        
    context = {'title':'Edit Clip', 'form': form}
    return render(request, 'base/edit.html', context)

def deleteClip(request, pk):
    soundclip = SoundClip.objects.get(id=pk)

    if request.method == 'POST':
        soundclip.delete()
        return redirect('home')
    
    context = {'obj': soundclip}
    return render(request, 'base/delete.html', context)

def uploadClip(request):
    form = SoundclipForm()

    if request.method == 'POST':
        form = SoundclipForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'title': 'Upload Clip', 'form': form}
    return render(request, 'base/edit.html', context)

def test(request):
    return HttpResponse("Test")