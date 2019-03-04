from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Ticket, Trip
from django.http import Http404
from django.shortcuts import get_object_or_404

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def details_page(request):
    if request.method == 'GET':
        end_station_id = request.GET.get('station')
    elif request.method == 'POST':
        end_station_id = request.POST.get('to_station')
    #print(request.GET.get('to_station'))
    trips = Trip.objects.filter(end_station_id=end_station_id)
    context = {'trips' : trips}
    return render(request, 'details/details.html', context)
    

def trips_page(request, trip_id):
    trip = get_object_or_404( Trip,pk=trip_id)
    error = None
    ticket = None
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        ticket = Ticket(trip=trip,first_name=first_name, middle_name=middle_name,
            last_name=last_name, email=email,gender=gender)
        try:
            ticket.full_clean()
            ticket.save()
            return redirect('tickets',ticket_id=ticket.id)
        except ValidationError as e:
            error = dict(e)
            print(e)
    context = {'trip' : trip, 'error':error, 'ticket':ticket }
    return render(request, 'details/trips.html', context)
        


def tickets_page(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {'ticket' : ticket}
    return render(request, 'details/tickets.html', context)
    #return HttpResponse("Thank you !\n name: %s %s %s\n email: %s\n gender:%s" % (ticket.first_name, ticket.middle_name, ticket.last_name, ticket.email, ticket.get_gender_display()))



