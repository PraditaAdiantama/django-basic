from django.db import models

# Create your models here.
class Student(models.Model):
    nis = models.IntegerField()
    name = models.TextField()
    address = models.TextField()
    birth_date = models.DateField()
    