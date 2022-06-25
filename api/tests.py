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
