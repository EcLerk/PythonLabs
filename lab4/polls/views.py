from django.shortcuts import render
from .models import Driver, Service
from .forms import *

def index(request):
    services = Service.objects.all()
    drivers = Driver.objects.all()
    return render(request, 'polls/index.html', {'title': 'Главная страница', 'drivers': drivers,
                                                'services': services})


def login(request):
    return render(request, 'polls/../templates/registration/login.html')

def logged_out(request):
    return render(request, 'registration/logged_out.html')

