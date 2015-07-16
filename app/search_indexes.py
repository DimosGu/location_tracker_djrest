__author__ = 'baranbartu'

from haystack import indexes
from .models import Event
import datetime


class EventIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    plate = indexes.CharField(model_attr='plate')
    msisdn = indexes.CharField(model_attr='msisdn')
    location = indexes.CharField(model_attr='location')
    q = indexes.EdgeNgramField()

    @staticmethod
    def prepare_q(obj):
        return " ".join((
            obj.plate, obj.msisdn
        ))

    def get_model(self):
        return Event

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created_at__lte=datetime.datetime.now())

