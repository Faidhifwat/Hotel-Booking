from rest_framework import serializers
from .models import Hotel, Room

"""
Not sure if this is the proper way to use django rest framework
RoomDetail is for when getting the detail, maybe we can combine it
"""

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ['id', 'name', 'price_per_night']

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['hotel', 'room_num', 'total_customer']

class RoomDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'room_num', 'total_customer']
