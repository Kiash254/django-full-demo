from django.shortcuts import render
from .models import Customers,Products,Order,Tag
# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customers.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders':orders,
        'customers':customers,
        'total_orders':total_orders,
        'delivered':delivered,
    'pending':pending
    }
    return render(request, 'dashbord.html',context)
def products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products.html',context)
def customers(request,pk):
    customers = Customers.objects.get(id=pk)
    orders = customers.order_set.all()
    orders_count=orders.count()
    context={
        'customers':customers,
        'orders':orders,
        'orders_count':orders_count
        }
    
    return render(request, 'customers.html',context)