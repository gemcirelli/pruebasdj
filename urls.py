from django.conf.urls import url 
from Codigo.views import  horas_adelante
 
urlpatterns = [ 
    #url(r'^hola/$', hola), 
    #url(r'^fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_adelante), 
] 