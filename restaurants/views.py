from django.shortcuts import render
from restaurants.models import Restaurant, Menu, Category, Product
# Create your views here.

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
