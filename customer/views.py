from django.shortcuts import render
from customer.serializers import CustomerSerializer
from django.http import JsonResponse

import logging
logger = logging.getLogger(__name__)

def create_customer(data):

    logger.debug("Creating customer for booking details")

    serializer = CustomerSerializer(data=data)
    if serializer.is_valid():
        customer = serializer.save()
    return serializer
