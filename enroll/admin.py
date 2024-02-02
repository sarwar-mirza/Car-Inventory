from django.contrib import admin
from .models import ElectricCar, GasCar

# Register your models here(EleactricCar).
@admin.register(ElectricCar)
class ElectricCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'make', 'model', 'year', 'battery_range']


# Register your models here(GasCar).
@admin.register(GasCar)
class GasCarAdmin(admin.ModelAdmin):
    list_display = ['id', 'make', 'model', 'year', 'fuel_efficiency']
    

