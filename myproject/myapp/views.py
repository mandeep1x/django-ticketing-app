from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
# Create your views here.

def events_list(response):
    event = Event.objects.all()
    return HttpResponse(event)

def items_list(response):
    return HttpResponse("<h1>This is an Item view</h1>")    