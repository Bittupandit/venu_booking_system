from django.shortcuts import render

# Create your views here.

from .models import *

def home_page(request):
    qs = BookingSystem.objects.all()
    context = {'venues':qs}
    return render(request,'home_page.html',context)

def detail_page(request,pk):
    qs = BookingSystem.objects.get(pk=pk)
    context = {'venue':qs}
    return render(request,'detail_page.html',context)