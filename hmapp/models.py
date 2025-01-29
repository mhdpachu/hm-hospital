from django.db import models

# Create your models here.
class Treatment(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image')
    experience=models.CharField(max_length=100)
    fees=models.IntegerField()
    treatment=models.ForeignKey(Treatment, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.name
    


    





    

