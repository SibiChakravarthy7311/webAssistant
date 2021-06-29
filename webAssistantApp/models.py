from django.db import models

# Create your models here.


class pageElementModel(models.Model):
    id = models.IntegerField(primary_key=True)
    elementName = models.CharField(max_length=20)


class outlierElementModel(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    id = models.IntegerField()
