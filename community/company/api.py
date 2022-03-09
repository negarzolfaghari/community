from asyncio import exceptions
from concurrent.futures import thread
from datetime import datetime
from unittest import result
from django.forms import ValidationError
from rest_framework import response,status
from rest_framework import viewsets,views
from .models import Company
from info import models as pmodels
from . import serializers
class Companyviewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class=serializers.CompanySerializer
    # permission_classes=((IsSuperUserOrReadOnly,))
    def create(self, request, *args, **kwargs):
        data =request.data
        user={}
        user['first_name']=data.get('first_name')
        user['last_name']=data.get('last_name')
        user['phone']=data.get('phone')[0]
        user['email']=data.get('email')
        user['password']=data.pop('password')
        user['re_password']=data.pop('re_password')
        user['username']=data.get('national_code')
        data['username']=data.get('national_code')
        data['user'] =user
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ReportApiView(views.APIView):
    def post(self,request):
        company_id =request.query_params.get('id',0)
        try :
            from_date = datetime.strptime(self.request.data['from_date'],'%Y-%m-%d')
        except KeyError:
             raise ValidationError(datail='please enter from_date',code='from_date_missed')

        try :
            to_date=datetime.strptime(self.request.data['to_data'],'%Y-%m-%d')
        except KeyError:
            to_date=datetime.strptime(self.request.data.get('to_date',datetime.now().strftime('%Y-%m-%d')),'%Y-%m-%d') 
        from_date = datetime.strptime(self.request.data['from_date'],'%Y-%m-%d')
        to_date =datetime.strptime(self.request.data['to_date'],'%Y-%m-%d')
        from_date =from_date.replace(hour=0,minute=0,second=0,microsecond=0)
        to_date =to_date.replace(hour=23,minute=59,second=59,microsecond=0)
        

        count =pmodels.Person.objects.filter(company=company_id,created__gte=from_date,created__lte=to_date).count()
        result={}
        person_count =[]
        person_count.append(count)
        result['pcount']=person_count
        return response.Response(result)   

