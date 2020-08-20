from django.urls import path
from . import views

urlpatterns = [
            path('', views.create_booking, name='hotel_list'),
            path('<int:booking_id>', views.get_booking_details, name='get_booking_details'),
        ]
