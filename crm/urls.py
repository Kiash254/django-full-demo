from django.urls import path
from .views import home,products,customers,createOrder
app_name = 'crm'

urlpatterns = [
    path('',home,name='home'),
    path('products/',products,name='products'),
    path('customers/<int:pk>/',customers,name='customers'),
    path('create_order/',createOrder,name='create_order'),

]