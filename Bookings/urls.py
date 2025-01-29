from django.urls import path
from . import views
urlpatterns = [
    path('booking/<int:pk>/',views.booking,name='booking'),
    path('booked/',views.booked,name='booked'),
    path('success/',views.success,name='success'),
]