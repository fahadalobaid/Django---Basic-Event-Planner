from rest_framework import serializers
from .models import Event

class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["organizer" ,"name",  "email", "image",  "num_of_seats",  "booked_seats",  "start_date" , "end_date","id"]