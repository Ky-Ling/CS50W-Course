'''
Date: 2022-02-28 12:32:54
LastEditors: GC
LastEditTime: 2022-02-28 13:52:34
FilePath: \Django\lecture3\hello\views.py
'''
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello Brian!!")

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })