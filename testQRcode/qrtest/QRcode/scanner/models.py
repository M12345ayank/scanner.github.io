from django.db import models

# Create your models here.
class Register(models.Model):
    vehicle = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)


class Login(models.Model):
    vehicle = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    