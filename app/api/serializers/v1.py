from app.models import Event

__author__ = 'baranbartu'

from rest_framework import serializers


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ('plate', 'msisdn', 'location', 'created_at')