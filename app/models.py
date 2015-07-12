# Create your models here.
from django.db import models
from geoposition.fields import GeopositionField


class Event(models.Model):
    plate = models.CharField(max_length=11)
    msisdn = models.CharField(max_length=10)
    location = GeopositionField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s: %s,%s' % (self.plate, self.location.latitude, self.location.longitude)