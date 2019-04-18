from django.http import HttpResponse
from django.shortcuts import render
from details.models import Station, Ticket, Passenger

def homepage(request):
	stations = Station.objects.all()
	tickets = Ticket.objects.all()
	passengers = Passenger.objects.all()

	return render(request,'homepage.html',{'stations': stations, 'tickets': tickets, 'passengers': passengers})


#def about(request):
    #return HttpResponse('about')
    #return render(request, 'about.html')    