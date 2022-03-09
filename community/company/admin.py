from django.contrib import admin
from .models import Company
from django import forms
from django.contrib.gis.admin.options import OSMGeoAdmin

# Register your models here.


class Companyadminform(forms.ModelForm):
    class Meta :
        model = Company
        fields ='__all__'


class Companyadmin(OSMGeoAdmin) :
        form =Companyadminform
        list_display =['created', 'last_updated', 'name', 'phone', 'address_company', 'locations', 'locationtype']
        readonly_fields =['created','last_updated']

        
admin.site.register(Company,Companyadmin)

