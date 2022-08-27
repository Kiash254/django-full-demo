from django.urls import path
from .views import home,products,customers
app_name = 'crm'

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('customers/<int:pk>/',customers,name='customers'),
]