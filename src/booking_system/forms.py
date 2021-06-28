from django import forms
from django.db.models import fields

from . models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'name',
            'booking_person_name',
            'email',
            

        ]