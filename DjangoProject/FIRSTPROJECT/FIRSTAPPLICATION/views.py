from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstview(request):
    return HttpResponse('Hi, This is running from FirstApplication')

def customwebpage(request):
    context = {"tag_var":"Hi"}
    return render(request,"demo.html",context)