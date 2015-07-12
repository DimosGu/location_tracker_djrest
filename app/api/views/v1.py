__author__ = 'baranbartu'

from app.models import Event
from app.api.serializers.v1 import EventSerializer
from rest_framework import viewsets
from haystack.query import SearchQuerySet
import simplejson as json
from django.http import HttpResponse


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'search':
            return self.search(request)
        else:
            return super(EventViewSet, self).retrieve(request, *args, **kwargs)

    def search(self, request):
        q = request.GET.get('q', '')
        sqs = SearchQuerySet().autocomplete(q=q)
        events = [{'plate': result.plate, 'msisdn': result.msisdn, 'location': result.location} for result in sqs]
        return HttpResponse(json.dumps(events), content_type='application/json')