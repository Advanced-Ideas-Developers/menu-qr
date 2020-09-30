from django.urls import path
from .views import home, success_view

urlpatterns = [
  path('', home, name='home'),
  path('success/', success_view, name='success'),
]