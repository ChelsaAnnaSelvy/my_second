from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request,'home/home.html')

def registerView(request):
    return render(request,'home/signup.html')

def loginView(request):
    return render(request,'home/login.html')
