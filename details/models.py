from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
def validate_string(value):
    if value.isalpha():
        print('Good')
    else:
        raise ValidationError(
            ('Enter a valid name!'),
            params={'value': value},
        )

class Station(models.Model):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return "{}".format(self.name)




class Train(models.Model):
    name = models.CharField(null=True, max_length=100)
    seats = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)



class Trip(models.Model):
    train = models.ForeignKey(Train, related_name="trip_train", null=True, on_delete=models.CASCADE)
    start_station = models.ForeignKey(Station, related_name="start_station" ,on_delete=models.CASCADE, null=True)
    end_station = models.ForeignKey(Station, related_name="end_station" ,on_delete=models.CASCADE, null=True)
    start_time_date = models.DateTimeField()
    end_time_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return "Start: {} - End: {} - Train: {}".format(self.start_station, self.end_station, self.train)



class Ticket(models.Model):
    GENDER = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    trip = models.ForeignKey(Trip, related_name="tickets", null=True, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True, blank=True)
    first_name = models.CharField(validators=[validate_string], null=True, max_length=100, blank=False)
    middle_name = models.CharField(validators=[validate_string], null=True, max_length=100, blank=False)
    last_name = models.CharField(validators=[validate_string], null=True, max_length=100, blank=False)
    email = models.EmailField(max_length=70,blank=True, null= True)
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return "{}".format(self.first_name)



"""class Passenger(models.Model):
    TICKETS_NUMBER = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
    )
    
    
    tickets_number = models.IntegerField(default=1, choices=TICKETS_NUMBER)
    #ticket_ptr = models.OneToOneField(null=True, auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=False, serialize=False, to='details.Ticket')
    def __str__(self):
        return "{}".format(self.tickets_number)"""







