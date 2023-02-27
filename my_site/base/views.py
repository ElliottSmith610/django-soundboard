from django.shortcuts import render, redirect
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name': 'Fridays With Pewdiepie'},
    {'id': 2, 'name': 'I love memes'},
    {'id': 3, 'name': 'Cor yeah mate'},
]

def home(request):
    return redirect('soundboard')

def soundboard(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def test(request):
    return HttpResponse("Test")