from django.db import models

# Create your models here.
class reg_student(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    date = models.DateField()

