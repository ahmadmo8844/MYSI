from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("hello, workd!")
    def brain (request):
        return HttpResponse("hello, Brian!")

def david (request):
    return HttpResponse("Hello, david!")
    