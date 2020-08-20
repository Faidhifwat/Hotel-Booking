from django.shortcuts import render
from django.http import JsonResponse
from .serializers import HotelSerializer, RoomSerializer
from .models import Hotel

import random
import string

import logging
logger = logging.getLogger(__name__)

def hotel_list(request):

    if request.method == "GET":
        logger.info("Get all list of hotels")
        all_hotels = Hotel.objects.all()
        serializer = HotelSerializer(all_hotels, many=True)
        return JsonResponse(serializer.data, safe=False)

def create_room(data):
    """
    Since we dont have a proper Hotel/Room data model,
    we are going to generate a simple random room number
    """
    letter = random.choice(string.ascii_uppercase)
    number = str(random.randint(1,14))
    room_number = letter + number

    data.update({"room_num": room_number})

    serializer = RoomSerializer(data=data)
    if serializer.is_valid():
        serializer.save()

    return serializer
