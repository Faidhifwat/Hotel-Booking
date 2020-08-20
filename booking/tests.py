from django.test import TestCase, Client
from unittest.mock import ANY

from .models import BookingDetail
from hotel.models import Hotel
from .views import create_booking

class BookingTest(TestCase):

    def setUp(self):
        self.client = Client()
        hotel = Hotel.objects.create(name="Testing Hotel", price_per_night=80)

        self.data = {"hotel": hotel.pk,
                    "total_customer": 2,
                    "check_in_date": "07-07-2020",
                    "check_out_date": "07-08-2020",
                    "customer":{"name": "Ifwat",
                      "email": "faidhi@ifwat.com",
                      "phone_number": "012345678"}}

    def test_create_booking(self):

        expected_value = {'id': 1,
                'customer': 1,
                'hotel': 1,
                'room': 1,
                'check_in_date': '2020-07-07T12:00:00Z',
                'check_out_date': '2020-07-08T14:00:00Z',
                'total_amount': 80,
                'payment_success': True,
                'recorded_at': ANY}

        create_order = self.client.post('/booking/', self.data, content_type='application/json')
        self.assertEqual(200, create_order.status_code)
        self.assertEqual(expected_value, create_order.json())

    def test_get_booking_detail(self):

        expected_value = {'customer':{'name': 'Ifwat',
                    'email': 'faidhi@ifwat.com',
                    'phone_number': '012345678'},
                    'hotel':{'id': 1,
                        'name': 'Testing Hotel',
                        'price_per_night': '80.00'},
                    'room':{'id': 1,
                        'room_num': ANY,
                        'total_customer': 2},
                    'check_in_date': '2020-07-07T12:00:00Z',
                    'check_out_date': '2020-07-08T14:00:00Z',
                    'total_amount': 80,
                    'payment_success': True,
                    'recorded_at': ANY}

        create_order = self.client.post('/booking/', self.data, content_type='application/json')
        booking = self.client.get('/booking/1')
        self.assertEqual(200, booking.status_code)
        self.assertEqual(expected_value, booking.json())
