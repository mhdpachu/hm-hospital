from django.shortcuts import render,redirect,get_list_or_404
from . models import Treatment,Doctor


# Create your views here.
def home(request):
    return render(request,'home.html')

def treatment(request):
    treatment=Treatment.objects.all()
    return render(request,'treatment.html',{'treatment':treatment})


def doctor(request,treatment_id):
    treat=get_list_or_404(Doctor,treatment_id=treatment_id)
    return render(request,'doctor.html',{'treat':treat})




