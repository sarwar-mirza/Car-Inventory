from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    
    class Meta:
        abstract = True


class ElectricCar(Car):
    battery_range = models.IntegerField()


class GasCar(Car):
    fuel_efficiency = models.IntegerField()

