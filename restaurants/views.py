from django.views.generic import TemplateView

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from restaurants.models import Restaurant, Plan, PlanDetail, Menu, Category, Product

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
        'name', 'foto_restaurante', 'foto_portada', 'link', 'foto_qr', 'id').filter(restaurant_test=True)
    planes = Plan.objects.values('name', 'price')
    detalles_planes = PlanDetail.objects.select_related('plan_id')
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                context = {
                    'name': name,
                    'phone': phone,
                    'from_email': from_email,
                    'message': message
                }
                html_message = render_to_string('general/email.html', context)
                send_mail(
                    'Mensaje de contacto Menús QR', message, from_email, ['info@ai-devs.com'], html_message=html_message
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    context = {
        'all': restaurants,
        'planes': planes,
        'detalles': detalles_planes,
        'form': form
    }
    return render(request, 'general/index.html', context)


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def menu(request, link):
    restaurant = Restaurant.objects.get(link=link)
    restaurant_id = restaurant.id
    menu_id = Menu.objects.get(restaurant=restaurant_id).id
    categorias = Category.objects.filter(
        menu_id=menu_id).select_related('menu_id')
    productos = Product.objects.select_related('category_id')

    context = {
        'restaurant': restaurant,
        'categories': categorias,
        'products': productos
    }
    return render(request, 'restaurants/menu.html', context)
