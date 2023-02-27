from django.shortcuts import render, redirect

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