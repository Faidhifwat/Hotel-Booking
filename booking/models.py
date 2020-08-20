from django.db import models
from hotel.models import Hotel, Room
from customer.models import Customer

class BookingDetail(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField(blank=False, null=False)
    check_out_date = models.DateTimeField(blank=False, null=False)
    total_amount = models.PositiveIntegerField(blank=False, null=False)
    payment_success = models.BooleanField(default=False)
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
