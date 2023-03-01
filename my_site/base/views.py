from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import SoundClip, Message, Person
from .forms import MessageForm, SoundclipForm



def home(request):
    return redirect('soundboard')

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'User does not exist')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Username OR password does not exist')
        

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # commit=false 'freezes' the saved user object so we can tinker with additional parameters
            user = form.save(commit=False) 
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')


    context = {'page': page, 'form': form}
    return render(request, 'base/login_register.html', context)

def soundboard(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    sounds = SoundClip.objects.filter(
        # | used for or statements, & for and
        # Returns searches if it matches a person or a title
        Q(person__name__icontains=q) | 
        Q(title__icontains=q)
        )
    person = Person.objects.all()
    sound_count = sounds.count()
    sound_messages = Message.objects.all()[:10]

    context = {
        'sounds': sounds,
        'people': person,
        'sound_count': sound_count,
        'sound_messages': sound_messages,
        }
    return render(request, 'base/home.html', context)

def individual_clip(request, pk):
    sound = SoundClip.objects.get(id=pk)
    # To get a child of an object, use lowercase starting letter
    comments = sound.message_set.all() # many2one use _set.all()
    commenters = sound.commenters.all() # many2many can just use .all()
    form = MessageForm()

    if request.method == 'POST':
        # form = MessageForm(request.POST)
        # form.user

        if request.POST.get('body') != '':
            message = Message.objects.create(
                user=request.user,
                soundclip=sound,
                body=request.POST.get('body')
            )
            #message.save()
            sound.commenters.add(request.user)
            return redirect('individual_clip', pk=sound.id)

    context = {
        'sound': sound,
        'comments': comments,
        'commenters': commenters,
        'form': form,
        }
    return render(request, 'base/clip_card.html', context)

@login_required(login_url='/login')
def deleteComment(request, pk):
    comment = Message.objects.get(id=pk)


    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    
    context = {'obj': comment}
    return render(request, 'base/delete.html', context)

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def deleteClip(request, pk):
    soundclip = SoundClip.objects.get(id=pk)

    if request.method == 'POST':
        soundclip.delete()
        return redirect('home')
    
    context = {'obj': soundclip}
    return render(request, 'base/delete.html', context)

@login_required(login_url='/login')
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