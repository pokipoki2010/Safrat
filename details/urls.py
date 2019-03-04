from django.urls import path, include, re_path

from . import views

urlpatterns = [
   
    path('tickets/<int:ticket_id>/',views.tickets_page, name='tickets'),
    path('trips/<int:trip_id>/',views.trips_page, name='trips'),
    re_path(r'^from/(?P<start_station>[0-9]{1,50})/$', views.details_page, name='details_page'),
 	path('', views.details_page, name='booking'),    
]