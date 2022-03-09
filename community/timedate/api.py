from concurrent.futures import thread
from datetime import datetime
from unittest import result
from django.forms import ValidationError
from rest_framework import response,status
from rest_framework import viewsets,views
from .models import TakeTime
from info import models as pmodels
from datetime import date
from . import models
import calendar
from . import serializers
from django.utils.dateparse import parse_date

class Taketimeviewset(viewsets.ModelViewSet):
    queryset = TakeTime.objects.all()
    serializer_class=serializers.TaketimeSerializer
    # permission_classes=((IsSuperUserOrReadOnly,))
    def create(self, request, *args, **kwargs):
        data =request.data    
        curr_date = data.get('date')
        curr_date=parse_date(curr_date)
        day_of_week=calendar.day_name[curr_date.weekday()]
        data['day']=day_of_week
        _time=data.get('time')
        _date=data.get('date')
        datetime,created=models.TakeTime.objects.get_or_create(time=_time, date=_date,defaults={"day":day_of_week,"is_active":True})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    
