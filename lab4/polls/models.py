import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Driver(models.Model):
    name = models.CharField('Имя', max_length=20)
    surname = models.CharField('Фамилия', max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Vehicle(models.Model):
    brand = models.CharField('бренд', max_length=20)
    model = models.CharField('модель', max_length=20)
    year = models.IntegerField('год выпуска', validators=[MinValueValidator(1980), MaxValueValidator(2023)])

    def __str__(self):
        return f"{self.brand} {self.model}, {self.year}"

class Service(models.Model):
 #   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('наименование услуги', max_length=40)
    description = models.TextField('описание услуги')
    def __str__(self):
        return self.title

class Order(models.Model):
  #  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    orderDate = models.DateField('время заказа', auto_now=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return f"заказ №{self.id}"


