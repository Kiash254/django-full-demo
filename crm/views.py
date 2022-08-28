from django.shortcuts import render,redirect
from .models import Customers,Products,Order,Tag
from .forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def Register(request):
    form = CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'register.html',context)

def Login(request):
    return render(request,'login.html')

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
    myFilter=OrderFilter(request.GET,queryset=orders)
    orders=myFilter.qs
    context={
        'customers':customers,
        'orders':orders,
        'orders_count':orders_count,
        'myFilter':myFilter
        }
    
    return render(request, 'customers.html',context)


def createOrder(request,pk):
    OrderFormSet=inlineformset_factory(Customers,Order, fields=('product', 'status'), extra=10)
    customer=Customers.objects.get(id=pk)
    # form = OrderForm(initial={'customer':customer})
    formset=OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method=='POST':
        # form = OrderForm(request.POST)
        formset=OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('crm:home')
    context = {
        'formset':formset
    }
    return render(request, 'order_form.html',context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method=='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('crm:home')
    context = {
        'form':form
    }
    return render(request, 'order_form.html',context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('crm:home')
    context = {
        'item':order
    }
    return render(request, 'delete.html',context)