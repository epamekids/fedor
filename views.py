from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fedor (request):
    return HttpResponse("it's me")