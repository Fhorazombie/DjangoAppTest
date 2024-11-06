from django.shortcuts import render
from django.http import HttpResponse

def module1_view(request):
    return HttpResponse("This is Module 1")