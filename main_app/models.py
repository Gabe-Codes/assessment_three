from django.db import models


class Widget(models.Model):
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()

