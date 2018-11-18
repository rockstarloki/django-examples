from django.db import models

class MyProduct(models.Model):
    no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)

