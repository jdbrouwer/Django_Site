from django.shortcuts import render

# a basic poll view from django.as

from django.http import HttpResponse

def index(request):
    return HttpResponse(" Hello world, Welcome to my poll")
