from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
context = {
        'name' : "subash mandal",
        'age' : 24
    }

def home(request):
    return render(request, 'home.html', context)

def profile(request):
    return render(request, 'profile.html', context)