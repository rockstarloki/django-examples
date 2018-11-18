from django.db import models

class Commentdetails(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=50)

