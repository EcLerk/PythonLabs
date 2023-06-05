from django.shortcuts import render
from .models import Driver, Service


def index(request):
    services = Service.objects.all()
    drivers = Driver.objects.all()
    return render(request, 'polls/index.html', {'title': 'Главная страница', 'drivers': drivers,
                                                'services': services})
# Create your views here.

