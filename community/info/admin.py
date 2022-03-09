from django.contrib import admin
from info.models import Person
from django import forms
from django.contrib.gis.admin.options import OSMGeoAdmin

# Register your models here.

class Personadminform(forms.ModelForm):
    class Meta :
        model = Person
        fields ='__all__'


class Personadmin(OSMGeoAdmin) :
        form =Personadminform
        list_display =['created','company', 'last_updated', 'first_name', 'last_name', 'gender', 'user','father_name', 'birth_place', 'place_issuance_identitycard', 'birth_date', 'identity_number', 'identity_serial_number', 'national_code', 'education', 'job', 'work_address', 'home_address', 'mobile_number', 'phone_number', 'aviculter_address', 'postalcode', 'township','locations' ]
        readonly_fields =['created','last_updated']

        
admin.site.register(Person,Personadmin)
