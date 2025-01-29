from django.contrib import admin
from . models import Booking
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=['name','age','number','gender','doctor']

admin.site.register(Booking,BookAdmin)