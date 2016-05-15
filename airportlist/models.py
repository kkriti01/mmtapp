from __future__ import unicode_literals

from django.db import models


class Airports(models.Model):
    code = models.CharField(max_length=225)
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=225)
    rating = models.FloatField()
    city = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    state = models.CharField(max_length=225)
    tz = models.CharField(max_length=225)
    type = models.CharField(max_length=225)
    url = models.CharField(max_length=225)
    elev = models.CharField(max_length=225)
    direct_flights = models.CharField(max_length=225)

