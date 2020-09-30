from django.urls import path
from django.contrib import admin
from .views import menu

urlpatterns = [
    path('menu/<link>', menu, name='menu')
]
