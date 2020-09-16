from django.urls import path
from .views import LasTejitasView, HongKongView, TacontentoView

urlpatterns = [
  path('las-tejitas/', LasTejitasView.as_view(), name='las-tejitas'),
  path('hong-kong/', HongKongView.as_view(), name='hong-kong'),
  path('tacontento/', TacontentoView.as_view(), name='tacontento'),
]