from itertools import count
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import datetime


@cache_page(60 * 2)
@api_view(['GET'])
def get_weather_query_string(request):
    city = request.GET.get('city')
    country = request.GET.get('country')

    if city is None or country is None:
        return Response("Invalid URL format. Query paremeters are missing.", status=status.HTTP_400_BAD_REQUEST)

    res = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032').json()

    if res['cod'] != 200:
        return Response(res, status=status.HTTP_404_NOT_FOUND)

    requested_time = datetime.datetime.utcfromtimestamp(
        res['dt']) + datetime.timedelta(seconds=res['timezone'])

    sunrise = datetime.datetime.utcfromtimestamp(
        res["sys"]["sunrise"]) + datetime.timedelta(seconds=res['timezone'])
    sunset = datetime.datetime.utcfromtimestamp(
        res["sys"]["sunset"]) + datetime.timedelta(seconds=res['timezone'])

    dirs = ['north', 'north-northeast', 'northeast', 'east-northeast', 'east', 'east-southeast', 'southeast', 'south-southeast',
            'south', 'south-southwest', 'southwest', 'west-southwest', 'west', 'west-northwest', 'northwest', 'north-northwest']
    ix = round(res["wind"]["deg"] / (360. / len(dirs)))
    wind_direction = dirs[ix % len(dirs)]

    data = {
        'location_name': f'{res["name"]}, {res["sys"]["country"]}',
        'temperature': f'{int(round(res["main"]["temp"] - 273.15))} °C',
        'wind': f'{res["weather"][0]["description"].capitalize()}, {res["wind"]["speed"]} m/s, {wind_direction}',
        'cloudiness': f'{res["weather"][0]["main"].capitalize()}',
        'pressure': f'{res["main"]["pressure"]} hpa',
        'humidity': f'{res["main"]["humidity"]}%',
        'sunrise': sunrise.strftime("%H:%M"),
        'sunset': sunset.strftime("%H:%M"),
        'geo_coordinates': f'[{round(res["coord"]["lat"], 2)}, {round(res["coord"]["lon"], 2)}]',
        'requested_time': requested_time.strftime("%Y-%m-%d %H:%M:%S"),
        'forecast': {
            'feels_like': f'{int(round(res["main"]["feels_like"]) - 273.15)} °C',
            'temp_min': f'{int(round(res["main"]["temp_min"]) - 273.15)} °C',
            'temp_max': f'{int(round(res["main"]["temp_max"]) - 273.15)} °C',
            'humidity': f'{res["visibility"] / 1000} km',
            'temperature_in_fahrenheit': f'{int(round((res["main"]["temp"] - 273.15) * 9/5 + 32))} °C',
        },
    }

    return Response(data, status=status.HTTP_200_OK)


@cache_page(60 * 2)
@api_view(['GET'])
def get_weather(request, city, country):
    res = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid=1508a9a4840a5574c822d70ca2132032').json()

    if res['cod'] != 200:
        return Response(res, status=status.HTTP_404_NOT_FOUND)

    requested_time = datetime.datetime.utcfromtimestamp(
        res['dt']) + datetime.timedelta(seconds=res['timezone'])

    sunrise = datetime.datetime.utcfromtimestamp(
        res["sys"]["sunrise"]) + datetime.timedelta(seconds=res['timezone'])
    sunset = datetime.datetime.utcfromtimestamp(
        res["sys"]["sunset"]) + datetime.timedelta(seconds=res['timezone'])

    dirs = ['north', 'north-northeast', 'northeast', 'east-northeast', 'east', 'east-southeast', 'southeast', 'south-southeast',
            'south', 'south-southwest', 'southwest', 'west-southwest', 'west', 'west-northwest', 'northwest', 'north-northwest']
    ix = round(res["wind"]["deg"] / (360. / len(dirs)))
    wind_direction = dirs[ix % len(dirs)]

    data = {
        'location_name': f'{res["name"]}, {res["sys"]["country"]}',
        'temperature': f'{int(round(res["main"]["temp"] - 273.15))} °C',
        'wind': f'{res["weather"][0]["description"].capitalize()}, {res["wind"]["speed"]} m/s, {wind_direction}',
        'cloudiness': f'{res["weather"][0]["main"].capitalize()}',
        'pressure': f'{res["main"]["pressure"]} hpa',
        'humidity': f'{res["main"]["humidity"]}%',
        'sunrise': sunrise.strftime("%H:%M"),
        'sunset': sunset.strftime("%H:%M"),
        'geo_coordinates': f'[{round(res["coord"]["lat"], 2)}, {round(res["coord"]["lon"], 2)}]',
        'requested_time': requested_time.strftime("%Y-%m-%d %H:%M:%S"),
        'forecast': {
            'feels_like': f'{int(round(res["main"]["feels_like"]) - 273.15)} °C',
            'temp_min': f'{int(round(res["main"]["temp_min"]) - 273.15)} °C',
            'temp_max': f'{int(round(res["main"]["temp_max"]) - 273.15)} °C',
            'humidity': f'{res["visibility"] / 1000} km',
            'temperature_in_fahrenheit': f'{int(round((res["main"]["temp"] - 273.15) * 9/5 + 32))} °C',
        },
    }

    return Response(data, status=status.HTTP_200_OK)
