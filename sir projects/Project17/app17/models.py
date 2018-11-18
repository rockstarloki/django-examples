from django.db import models

class PrinciData(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cno = models.IntegerField()
    email = models.EmailField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)

class FacultyDetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    cno = models.IntegerField()
    subject = models.CharField(max_length=50)
    exp = models.IntegerField()
    email = models.EmailField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)