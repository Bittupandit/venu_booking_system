from django.shortcuts import redirect, render

# Create your views here.

from .models import *
from .forms import *
def home_page(request):
    qs = BookingSystem.objects.all()
    context = {'venues':qs}
    return render(request,'home_page.html',context)

def detail_page(request,pk):
    qs = BookingSystem.objects.get(pk=pk)
    context = {'venue':qs}
    return render(request,'detail_page.html',context)

def booking_form(request,pk):
    venue = BookingSystem.objects.get(id=pk)
    print(venue)
    form = BookingForm(initial={'name':venue})
    # import pdb;
    # pdb.set_trace()
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('detail-page',venue.id)
    context = {'form':form}
    return render(request,'booking_form.html',context)


def booking_list(request):
    bookings = Booking.objects.all()
    context = {"bookings":bookings}
    return render(request,'booking_list.html',context)