
from django.db import models
from hmapp.models import Doctor
# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    number=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
