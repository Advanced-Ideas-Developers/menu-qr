from django.views.generic import TemplateView

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from restaurants.models import Restaurant, Plan, PlanDetail

from restaurants.forms import ContactForm

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
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['paulsotelo97@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'general/index.html', {'all': restaurants, "planes": planes, "detalles": detalles_planes, 'form': form})

# def contactView(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
