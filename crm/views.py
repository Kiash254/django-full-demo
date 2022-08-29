from django.shortcuts import render,redirect
from .models import Customers,Products,Order,Tag
from .forms import OrderForm, CreateUserForm,CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout   
from django.contrib.auth.decorators import login_required
# Create your views here.
def Register(request):
    if request.user.is_authenticated:
        return redirect('crm:home')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user=form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('crm:login')
        context = {'form':form}
        return render(request, 'register.html',context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('crm:home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('crm:home')
            else:
                messages.info(request,'Username or Password is incorrect')
        return render(request,'login.html')


def Logoutview(request):
    logout(request)
    return redirect('crm:login')
@login_required(login_url='crm:login')
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
@login_required(login_url='crm:login')
def products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products.html',context)
@login_required(login_url='crm:login')
def Userpage(request):
    orders = request.user.customers.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {
        'orders':orders,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending
    }
    return render(request, 'user.html',context)
@login_required(login_url='crm:login')
def Account(request):
    customers= request.user.customers
    form=CustomerForm(instance=customers)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=customers)
        if form.is_valid():
            form.save()

    context={
        'form':form
    }
    return render(request,'settings.html',context)
@login_required(login_url='crm:login')
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

@login_required(login_url='crm:login')
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
@login_required(login_url='crm:login')
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
@login_required(login_url='crm:login')
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('crm:home')
    context = {
        'item':order
    }
    return render(request, 'delete.html',context)