from django.urls import path
from django.contrib import admin
from .views import LasTejitasView, HongKongView, TacontentoView, successView, menu

urlpatterns = [
    path('las-tejitas/', LasTejitasView.as_view(), name='las-tejitas'),
    path('hong-kong/', HongKongView.as_view(), name='hong-kong'),
    path('tacontento/', TacontentoView.as_view(), name='tacontento'),
    path('success/', successView, name='success'),
    path('menu/<link>', menu)
]
