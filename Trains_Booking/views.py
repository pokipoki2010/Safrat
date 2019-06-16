from django.http import HttpResponse
from django.shortcuts import render
from details.models import Station, Ticket

def homepage(request):
	stations = Station.objects.all()
	tickets = Ticket.objects.all()
	#passengers = Passenger.objects.all()
	context = {'station': stations, 'ticket': tickets}
	return render(request,'homepage.html', context)


#def about(request):
    #return HttpResponse('about')
    #return render(request, 'about.html')    