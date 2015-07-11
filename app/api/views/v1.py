__author__ = 'baranbartu'

from app.models import Event
from app.api.serializers.v1 import EventSerializer
from rest_framework import viewsets


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
