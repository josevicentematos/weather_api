from django.urls import path
from . import views

urlpatterns = [
    path('weather/<str:city>/<str:country>',
         views.get_weather, name="weather"),

    path('weather',
         views.get_weather_query_string, name="weather_query_string"),
]
