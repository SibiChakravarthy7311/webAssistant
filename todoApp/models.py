from django.db import models

# Create your models here.


class TodoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=20)
