from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    profile_pic = models.ImageField(default='kiash.jpg',null=True,blank=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name=models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.name
class Products(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    name=models.CharField(max_length=200,blank=True,null=True)
    price=models.FloatField(blank=True,null=True)
    category=models.CharField(max_length=200,blank=True,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,blank=True,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tag=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey(Customers,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200,blank=True,null=True,choices=STATUS)
    note=models.CharField(max_length=1000,blank=True,null=True)


    def __str__(self):
        return self.product.name
   