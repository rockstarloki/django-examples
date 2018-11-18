from django.db import models


class  Emp(models.Model):
    idno = models.IntegerField()
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    salary = models.DecimalField(max_digits=7,decimal_places=2)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)

