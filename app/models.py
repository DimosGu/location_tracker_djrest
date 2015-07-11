# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from geoposition.fields import GeopositionField


class Event(models.Model):
    plate = models.CharField(max_length=11)
    msisdn = PhoneNumberField()
    location = GeopositionField()
    created_at = models.DateTimeField(auto_now_add=True)