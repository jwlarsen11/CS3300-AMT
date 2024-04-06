from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def calculator(request):
    return render(request, 'app/calculator.html')

def forum(request):
    return render(request, 'app/forum.html')

def login(request):
    return render(request, 'app/login.html')