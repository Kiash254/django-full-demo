from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customers 

def customer_profile(sender,instance,created,**kwargs):
    if created:
       Customers.objects.create(
                    user=instance,
                    name=instance.username,
                )
post_save.connect(customer_profile,sender=User)
