from django.db import models


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Orders(models.Model):
    username = models.CharField(max_length=20)
    cart = models.CharField(max_length=500)
    price = models.IntegerField()

class Cart(models.Model):
    username = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    toppings = models.CharField(max_length=10)
    sides = models.CharField(max_length=10)
    drink =  models.CharField(max_length=10)
    deserts = models.CharField(max_length=10)
    price = models.IntegerField()