from django.contrib import admin
from .models import Customers,Products,Order
# Register your models here.

admin.site.site_header = "CRM Admin"
admin.site.site_title = "CRM Admin Portal"
admin.site.index_title = "Welcome to CRM Admin Portal"

admin.site.register(Customers)
admin.site.register(Products)
admin.site.register(Order)

