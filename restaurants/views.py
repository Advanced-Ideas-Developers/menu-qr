from django.views.generic import TemplateView
from django.shortcuts import render

from restaurants.models import Restaurant, Plan, PlanDetail

# Create your views here.


class LasTejitasView(TemplateView):
    template_name = 'restaurants/las_tejitas.html'


class HongKongView(TemplateView):
    template_name = 'restaurants/hong_kong.html'


class TacontentoView(TemplateView):
    template_name = 'restaurants/tacontento.html'

# Soy un rebelde que usa funciones en lugar de clases osi


def index(request):
    restaurants = Restaurant.objects.values(
        'name', 'foto_restaurante', 'foto_portada', 'link', 'foto_qr')
    planes = Plan.objects.values('name', 'price')
    detalles_planes = PlanDetail.objects.select_related('plan_id')
    #print(str(planes.query))
    return render(request, 'general/index.html', {'all': restaurants, "planes": planes, "detalles": detalles_planes})
