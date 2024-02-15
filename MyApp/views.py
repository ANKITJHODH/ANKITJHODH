from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def about_us(request):
    return HttpResponse("Welcome to <B> 'MyApp' </B> Application")

