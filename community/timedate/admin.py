from django.contrib import admin
from .models import TakeTime


from django import forms

class Taketimeadminform(forms.ModelForm):
    class Meta :
        model = TakeTime
        fields ='__all__'


class Taketimeadmin(admin.ModelAdmin) :
        form =Taketimeadminform
        list_display =['pk','date', 'day', 'time', 'user1', 'is_active']
        

admin.site.register(TakeTime,Taketimeadmin)