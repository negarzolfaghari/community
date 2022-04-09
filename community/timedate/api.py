from concurrent.futures import thread
from datetime import datetime
from unittest import result
from django.forms import ValidationError
from rest_framework import response,status,viewsets,views
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

    def get_queryset(self):
        
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )
        if self.request.user.is_superuser:
            queryset=models.TakeTime.objects.all()
        else:
            queryset=models.TakeTime.objects.filter(is_active=True)
        return queryset

    def create(self, request, *args, **kwargs):
        data =request.data    
        time=data.get('time')
        moorning=['8-9','9-10','10-11','11-12']
        if time in moorning:
            moorningOrafter=True
        else :
            moorningOrafter=False
        curr_date = data.get('date')
        curr_date=parse_date(curr_date)
        day_of_week=calendar.day_name[curr_date.weekday()]
        data['day']=day_of_week
        _time=data.get('time')
        _date=data.get('date')
        datetime,created=models.TakeTime.objects.get_or_create(time=_time, date=_date,defaults={"day":day_of_week,"is_active":True,'moorningOrafter':moorningOrafter})
        # serializer = self.get_serializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        serializer =self.get_serializer(datetime)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


        
    
class ListTimeAPIView(views.APIView):
    def post(self,request):
        moorning_after_id=request.query_params.get('moorning_after_id',-1)
        moorning_after_id=int(moorning_after_id)
        if moorning_after_id==0:
            evening=models.TakeTime.objects.filter(moorningOrafter=False)
        elif moorning_after_id==1:
            evening=models.TakeTime.objects.filter(moorningOrafter=True)
        else:
            raise ValidationError(code="moorning_after_id is required",datail="please enter moorning_after_id")
        moorning_after_ser=serializers.TaketimeSerializer(evening,many=True)
        return response.Response(moorning_after_ser.data)

        
class SelectApiView(views.APIView):
    def post(self,request):
        time_id=request.query_params.get("time_id",0)
        if time_id==0:
            raise ValidationError(code="time_id is required",datail="please enter time_id")
        else :
            time=models.TakeTime.objects.filter(id=time_id)
            time_ser=serializers.TaketimeSerializer(time,many=True)
            time_ser.data[0]['is_active']=False
            time_ser.data[0]['user1']=request.user.id
            print(time_ser.data[0])
            return response.Response(time_ser.data)

            
            

    
