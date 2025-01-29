
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('treatment/',views.treatment,name='treatment'),
    path('doctor/<int:treatment_id>/',views.doctor,name='doctor'),
  
   
]