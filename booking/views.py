from django.shortcuts import render
from django.core import serializers
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from .models import BookingDetail
from hotel.serializers import RoomSerializer
from .serializers import BookingDetailSerializer
from hotel.models import Hotel
from booking.serializers import BookingSerializer
from django.views.decorators.csrf import csrf_exempt

from customer.views import create_customer
from hotel.views import create_room
from datetime import datetime, timedelta

import logging
logger = logging.getLogger(__name__)

def get_booking_details(request, booking_id):
    """
    Get the order details with specific booking id
    """

    if request.method == "GET":
        hotel = get_object_or_404(BookingDetail, pk=booking_id)
        serializer = BookingDetailSerializer(hotel, many=False)
        return JsonResponse(serializer.data)


@csrf_exempt
def create_booking(request):

    if request.method == "POST":

        logger.debug("Start creating booking")
        data = JSONParser().parse(request)

        #We will first check the customer params
        if data.get("customer"):

            customer = create_customer(data["customer"])

            if not customer.validated_data:
                return JsonResponse(customer.errors)
        else:
            return JsonResponse({"error": "customer field is required"}, status=400)

        if data.get("total_customer") and data.get("hotel"):

            room_data = {"hotel": data["hotel"], "total_customer": data["total_customer"]}
            room = create_room(room_data)

            if not room.validated_data:
                return JsonResponse(room.errors)
        else:
            return JsonResponse({"error": "total_customer field and hotel field is required"}, status=400)

        return handle_booking(data, customer, room)


def handle_booking(data, customer, room):
    """
    Aggregate data from customer and room
    Create the order
    output example:

        {'id: 13,
         'customer': 88,
         'hotel': 3,
         'room': 70,
         'check_in_date': '2020-07-07T12:00:00Z',
         'check_out_date': '2020-07-08T14:00:00Z',
         'total_amount': 80,
         'payment_success': True,
         'recorded_at': '2020-08-20T20:00:36.835428Z'}

    This will not return the FK field for customer, hotel, room
    """

    hotel = get_object_or_404(Hotel, pk=data['hotel'])

    #This is just really bad way to add time. Should have only use date
    check_in_date = datetime.strptime(data['check_in_date'], "%m-%d-%Y") + timedelta(hours=12)
    check_out_date = datetime.strptime(data['check_out_date'], "%m-%d-%Y") + timedelta(hours=14)

    total_day = check_out_date - check_in_date

    total_payment = calculate_total_payment(total_day.days, hotel.price_per_night)

    customer_id = customer.instance.pk
    room_id = room.instance.pk
    hotel_id = data['hotel']

    booking = {"hotel": hotel_id,
               "check_in_date": check_in_date,
               "check_out_date": check_out_date,
               "customer": customer_id,
               "total_amount": total_payment,
               "room": room_id,
               "payment_success": True}

    serializer = BookingSerializer(data=booking)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=200)
    return JsonResponse(serializer.errors)

def calculate_total_payment(days, price_per_night):
    """
    Payment should be on another app
    This is just to calculate the total price per night, should have more in this
    """
    total_payment = price_per_night * days
    return total_payment
