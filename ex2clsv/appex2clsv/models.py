from django.db import models

class Data(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    username = models.CharField(max_length=50)
    password  = models.CharField(max_length=50)
