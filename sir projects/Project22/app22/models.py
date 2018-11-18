from django.db import models

class CommentDetails(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField(primary_key=True)
    message = models.CharField(max_length=500)
