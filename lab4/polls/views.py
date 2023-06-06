from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Driver, Service, Order
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


class SingUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'polls/signup.html'


def orders(request):
    orders = Order.objects.all()
    return render(request, 'polls/orders.html', {'orders': orders})

