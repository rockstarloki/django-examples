from django.db import models

class Mydb(models.Model):
    no=models.IntegerField(max_length=15)
    name=models.CharField(max_length=21)
    price=models.IntegerField(max_length=10)

