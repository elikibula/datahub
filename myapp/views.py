from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'myapp/dashboard.html')


def aboutus(request):
    return render(request, 'myapp/aboutus.html')

# Create your views here.
