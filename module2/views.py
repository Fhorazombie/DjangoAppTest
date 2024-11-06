from django.shortcuts import render
from django.http import HttpResponse

def module2_view(request):
    return HttpResponse("This is Module 2")