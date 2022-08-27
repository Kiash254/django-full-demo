from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'dashbord.html')
def products(request):

    return render(request, 'products.html')
def customers(request):
    
        return render(request, 'customers.html')