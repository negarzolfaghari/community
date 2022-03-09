from django.contrib import admin
from ticket.models import Thread
from ticket.models import Message

from django import forms

# Register your models here.

class Threadadminform(forms.ModelForm):
    class Meta :
        model = Thread
        fields ='__all__'


class Threadadmin(admin.ModelAdmin) :
        form =Threadadminform
        list_display =['pk','created', 'category', 'ticket_id', 'user1', 'user2']
        readonly_fields =['created',]

class Messageadminform(forms.ModelForm):
    class Meta :
        model = Message
        fields ='__all__'


class Messageadmin(admin.ModelAdmin) :
        form =Messageadminform
        list_display =['pk','created', 'last_updated', 'message', 'file', 'status', 'direction', 'thread', ]
        readonly_fields =['created','last_updated']

        
        
admin.site.register(Thread,Threadadmin)
admin.site.register(Message,Messageadmin)


