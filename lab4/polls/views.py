from django.shortcuts import render
from .models import Driver

def index(request):
    drivers = Driver.objects.all()
    return render(request, 'polls/index.html', {'title': 'Главная страница', 'drivers': drivers})
# Create your views here.
