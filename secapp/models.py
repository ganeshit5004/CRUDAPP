from django.db import models

# Create your models here.
class student(models.Model):
    sno=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    std=models.CharField(max_length=5)