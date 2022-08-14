from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView
from .models import Event
from .serializers import EventListSerializer

class EventListView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

    
class UpdateListView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'