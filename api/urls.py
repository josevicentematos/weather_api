from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/<str:country>',
         views.get_weather, name="weather"),
]
