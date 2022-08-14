
from django.db import models
from django.forms import DateTimeField

class Event(models.Model):

    organizer = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    email =  models.EmailField(max_length=250)
    image =  models.CharField(max_length=250)
    num_of_seats =  models.DecimalField(max_digits=10,decimal_places=0)
    booked_seats =  models.DecimalField(max_digits=10,decimal_places=0)
    start_date =  models.DateTimeField(auto_now_add=True)
    end_date =  models.DateTimeField(auto_now_add=True)