from django.db import models

# Create your models here.

class person(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    user = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

class blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)