from django.contrib import admin
from .models import Infodoctor
from .models import Expertise

from django import forms
# from django.contrib.gis.admin.options import OSMGeoAdmin

# Register your models here.


class Doctoradminform(forms.ModelForm):
    class Meta :
        model = Infodoctor
        fields ='__all__'


class Doctoradmin(admin.ModelAdmin) :
        form =Doctoradminform
        list_display =['created', 'last_updated', 'first_name', 'last_name', 'gender', 'dr_code', 'mobile_phone', 'email', 'user', 'expertise']
        readonly_fields =['created','last_updated']



class Expertiseadminform(forms.ModelForm):
    class Meta :
        model = Expertise
        fields ='__all__'


class Expertiseadmin(admin.ModelAdmin) :
        form =Expertiseadminform
        list_display =['expertise']
        


        
admin.site.register(Infodoctor,Doctoradmin)
admin.site.register(Expertise,Expertiseadmin)

