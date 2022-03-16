from django.contrib import admin
from .models import Infosick

from django import forms
# from django.contrib.gis.admin.options import OSMGeoAdmin

# Register your models here.


class Sickadminform(forms.ModelForm):
    class Meta :
        model = Infosick
        fields ='__all__'


class Sickadmin(admin.ModelAdmin) :
        form =Sickadminform
        list_display =['created', 'last_updated', 'first_name', 'last_name', 'gender', 'national_code', 'mobile_phone', 'email', 'user']
        readonly_fields =['created','last_updated']

        
admin.site.register(Infosick,Sickadmin)

