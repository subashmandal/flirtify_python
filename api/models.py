from django.db import models

from django import requ

# Create your models here.
class Auther(models.Model):
    name = models.CharField()
    email = models.EmailField()

class Books(models.Model):
    Auther = models.CharField()
    publisher = models.models.ForeignKey(Auther, related_name='books', on_delete=models.CASCADE)
    publish_date = models.DateField()