from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    contact = models.IntegerField()
    comment = models.CharField(max_length=200)
