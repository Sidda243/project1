from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def siddhu(request):
    return  HttpResponse('<h1>Hello This is Siddhu!! How are you Doing?</h1>')

def karthik(request):
    return  HttpResponse('<marquee>Hello i am Karthik!! I am Doing Good....</marquee>')