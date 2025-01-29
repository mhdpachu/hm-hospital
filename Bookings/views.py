from django.shortcuts import render,get_list_or_404,redirect
from . models import Booking
from hmapp.models import Doctor
# Create your views here.

def booking(request,pk):
    products=get_list_or_404(Doctor ,pk=pk)
    return render(request,'book.html',{'products':products})

def booked(request):
    if request.method=="POST":
        d_id=request.POST.get('d_id')
        dname=Doctor.objects.get(pk=d_id)
        name=request.POST['name']
        age=request.POST['age']
        number=request.POST['number']
        gender=request.POST['gender']
        bookings=Booking(doctor=dname,name=name,age=age,number=number,gender=gender)
        bookings.save()
        return redirect('success')
    return redirect('booking')

def success(request):
    return render(request,'success.html')




