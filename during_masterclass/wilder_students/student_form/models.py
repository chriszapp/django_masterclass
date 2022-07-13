from django.db import models

# Create your models here.
class Student(models.Model):
    name =  models.CharField(max_length=200)# char/str
    age = models.IntegerField()# int
    city = models.CharField(max_length=100) # char/str