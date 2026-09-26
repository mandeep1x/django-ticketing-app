from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def events_list(response):
    return HttpResponse("Hello World")

def items_list(response):
    return HttpResponse("<h1>This is an Item view</h1>")    