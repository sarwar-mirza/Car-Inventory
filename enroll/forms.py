from django import forms
from .models import ElectricCar, GasCar


class ElectricCarForm(forms.ModelForm):
    class Meta:
        model = ElectricCar
        fields = ['make', 'model', 'year', 'battery_range']
        
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Car Name'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Model Name'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Year'}),
            'battery_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Battery Range'}),
        }


class GasCarForm(forms.ModelForm):
    
    class Meta:
        model = GasCar
        fields = ['make', 'model', 'year', 'fuel_efficiency']
        
        widgets = {
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Car Name'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Model Name'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Year'}),
            'fuel_efficiency': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your Fuel Efficiency'}),
        }
