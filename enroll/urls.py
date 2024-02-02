from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.ElectricCarTemplateView.as_view(), name='electric_car_page'),
    path('gascar/', views.GasCarView.as_view(), name='gas_car_page'),
]
