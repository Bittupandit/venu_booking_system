from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.


# booking system model...

class BookingSystem(models.Model):
    name = models.CharField(max_length=250,blank=True, null=True,verbose_name='Venu Name',help_text="Enter the Venue Name: ")
    venue_image = models.ImageField(upload_to = 'venu_image')
    address = models.CharField(max_length=300,blank=True, null=True,verbose_name="Address")
    landmark = models.CharField(max_length=100,blank=True, null=True,verbose_name="Landmark")
    available= models.BooleanField(blank=True, null=True,default=False)

    def __str__(self):
        return f'{self.name}'
