from django.contrib.gis.db import models


class Crop(models.Model):
    name = models.CharField(max_length=100)


class Farmer(models.Model):
    name = models.CharField(max_length=100)


class Season(models.Model):
    name = models.CharField(max_length=100)


class Field(models.Model):
    pole = models.PolygonField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE, default=1)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, default=1)
# Create your models here.
