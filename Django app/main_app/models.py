from django.db import models

class Postal(models.Model):
    id = models.AutoField(primary_key=True)
    lat = models.FloatField()
    lon = models.FloatField()
    