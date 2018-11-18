from django.db import models

class Princidetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=8)


class Facultydetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=8)

