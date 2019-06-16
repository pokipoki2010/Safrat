from django.contrib import admin
from .models import Station, Train, Ticket, Trip

admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Trip)
#admin.site.register(Passenger)

