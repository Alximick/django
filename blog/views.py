from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(requsert):
    return HttpResponse('Hello World')