from django.shortcuts import render
# Create your views here.
def signal(request):
    return render(request,'signal.html')