from django.test import TestCase
from model_mommy import mommy
import json

from .models import Flight, Airport


class FlightApiTestCase(TestCase):
    def setUp(self) -> None:
        self.flight_number = "TK1111"
        self.airport_1 = mommy.make(Airport)
        self.airport_2 = mommy.make(Airport)
        self.flight = mommy.make(Flight, flight_number=self.flight_number,
                                 from_airport=self.airport_1, to_airport=self.airport_2)

    def flight_info_view(self):
        from rest_framework.test import APIClient

        client = APIClient()
        response = client.post('/api/flight_info')
        self.assertEqual(response.status_code, 405)

        response_2 = client.get('/api/flight_info')
        self.assertEqual(response_2.status_code, 200)
        response_2_data = json.loads(response_2.content)
        self.assertEqual(len(response_2_data), 1)

        # Create new flight
        mommy.make(Flight)
        response_3 = client.get('/api/flight_info')
        response_3_data = json.loads(response_3.content)
        self.assertEqual(len(response_3_data), 2)
        for item in response_3_data:
            if item["flight_number"] == self.flight_number:
                self.assertEqual(item["count"], 1)

        # increase count of first flight
        mommy.make(Flight, flight_number=self.flight_number)
        response_4 = client.get('/api/flight_info')
        response_4_data = json.loads(response_4.content)
        self.assertEqual(len(response_4_data), 2)
        for item in response_4_data:
            if item["flight_number"] == self.flight_number:
                self.assertEqual(item["count"], 2)
