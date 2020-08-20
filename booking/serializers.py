from rest_framework import serializers
from hotel.serializers import HotelSerializer, RoomSerializer, RoomDetailSerializer
from customer.serializers import CustomerSerializer
from .models import BookingDetail

class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookingDetail
        fields = ['id', 'customer', 'hotel', 'room', 'check_in_date', 'check_out_date', 'total_amount', 'payment_success', 'recorded_at']

class BookingDetailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    room = RoomDetailSerializer()
    hotel = HotelSerializer()

    class Meta:
        model = BookingDetail
        fields = ['customer', 'hotel', 'room', 'check_in_date', 'check_out_date', 'total_amount', 'payment_success', 'recorded_at']
