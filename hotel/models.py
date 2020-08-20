from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price_per_night = models.DecimalField(max_digits=19, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_num = models.CharField(max_length=50, blank=False, null=False)
    total_customer = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.room_num
