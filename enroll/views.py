from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import ElectricCarForm, GasCarForm
from .models import ElectricCar, GasCar

# Create your views here.

class ElectricCarTemplateView(TemplateView):
    template_name = 'enroll/electriccar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = ElectricCarForm()
        power = ElectricCar.objects.all()
        context = {'form':fm, 'electric':power}
        return context
    
    
    def post(self, request):
        fm = ElectricCarForm(request.POST)
        
        if fm.is_valid():
            fm.save()
            fm = ElectricCarForm()
        power = ElectricCar.objects.all()
        return render(request, 'enroll/electriccar.html', {'form':fm, 'electric':power})


class GasCarView(View):
    def get(self, request):
        fm = GasCarForm()
        st = GasCar.objects.all()
        return render(request, 'enroll/gascar.html', {'form':fm, 'steam':st })
    
    def post(self, request):
        fm = GasCarForm(request.POST)
        
        if fm.is_valid():
            fm.save()
            fm = GasCarForm()
        st = GasCar.objects.all()
        return render(request, 'enroll/gascar.html', {'form':fm, 'steam':st })
    

