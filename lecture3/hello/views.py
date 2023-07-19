from django.http import HttpResponse
from django.shortcuts import render
#render is for html files
#HTTpResponse is to print wht we want

# Create your views here.
def index(request) : 
    return render(request, "hello/index.html")

def ivine(request) :
    return HttpResponse("Hello Ivine!")

def david(request) :
    return HttpResponse("Hello David!")

def greet(request, name) :
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })