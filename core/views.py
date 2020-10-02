from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.template.loader import render_to_string
from restaurants.models import Restaurant, Plan, PlanDetail
from .forms import ContactForm


# Create your views here.

def home(request):
    restaurants = Restaurant.objects.all().filter(restaurant_test=True)
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
                send_mail('Mensaje de contacto Menús QR', message, from_email, [
                          'info@ai-devs.com'], html_message=html_message)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    context = {
        'all': restaurants,
        'planes': planes,
        'detalles': detalles_planes,
        'form': form
    }
    return render(request, 'core/index.html', context)

def success_view(request):
    return HttpResponse('Success! Thank you for your message.')
