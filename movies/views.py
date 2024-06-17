from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Index")

def movies(request):
    return HttpResponse("Movies")

def movie_details(request, slug):
    return HttpResponse("Movie Detail: " + slug)