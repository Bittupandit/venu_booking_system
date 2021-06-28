from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField

# Create your models here.


# booking system model...

CITY_TYPE = (
    ('Delhi','Delhi'),
    ('Greate Noida','Greate Noida'),
    ('Lucknow','Lucknow'),
    ('Kanpur','Kanpur'),
    ('Muradabad','Muradabad'),
    ('Barabanki','Barabanki'),
    ('Varanasi','Varanasi'),
    ('Azamgarh','Azamgarh'),
    
)


class Location(models.Model):
    name = models.CharField(max_length=200,blank=True, null=True,verbose_name="Location Name")
    city = models.CharField(max_length=30,choices=CITY_TYPE,blank=True, null=True,verbose_name="City Name")

    def __str__(self):
        return f'{self.name}'

class BookingSystem(models.Model):
    name = models.CharField(max_length=250,blank=True, null=True,verbose_name='Venu Name',help_text="Enter the Venue Name: ")
    location = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True, null=True)
    venue_image = models.ImageField(upload_to = 'venu_image')
    address = models.CharField(max_length=300,blank=True, null=True,verbose_name="Address")
    landmark = models.CharField(max_length=100,blank=True, null=True,verbose_name="Landmark")
    available= models.BooleanField(blank=True, null=True,default=False)

    def __str__(self):
        return f'{self.name}'


class Booking(models.Model):
    name = models.ForeignKey(BookingSystem,on_delete=models.CASCADE,blank=True, null=True,verbose_name="Venue Name")
    booking_person_name = models.CharField(max_length=200,blank=True, null=True,verbose_name="Person Name")
    email = models.EmailField(blank=True, null=True)
    booking_date = models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
