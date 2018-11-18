from django.db import models

class UserRegister(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact = models.IntegerField()
    email = models.EmailField(max_length=100,primary_key=True)
    password = models.CharField(max_length=50)

