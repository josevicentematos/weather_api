from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class WeatherApiTests(APITestCase):
    def test_api_colombia(self):
        url = reverse('api:weather', kwargs={
                      'city': 'bogota', 'country': 'co'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['location_name'], 'Bogota, CO')

    def test_api_wrong_values(self):
        url = reverse('api:weather', kwargs={
                      'city': 'invalid_city', 'country': 'invalid_country'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_query_string_invalid(self):
        url = reverse('api:weather_query_string')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_api_query_string_valid(self):
        url = reverse('api:weather_query_string') + '?city=bogota&country=co'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['location_name'], 'Bogota, CO')

    def test_api_query_string_wrong_values(self):
        url = reverse('api:weather_query_string') + \
            '?city=invalid_country&country=invalid_country'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
