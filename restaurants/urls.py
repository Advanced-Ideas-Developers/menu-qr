from django.urls import path
from .views import LasTejitasView

urlpatterns = [
  path('las-tejitas/', LasTejitasView.as_view(), name='las-tejitas')
]