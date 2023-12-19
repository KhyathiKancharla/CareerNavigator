from django.db import models

# Create your models here.

class domain(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField()
    description=models.CharField(max_length=500)
    links=models.CharField(max_length=100)
    