from django.db import models

class Store(models.Model):
    store_owner = models.CharField(max_length=14)
    store_name = models.CharField(max_length=19)
    balance = models.FloatField(default=0)