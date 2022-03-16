from asyncio import exceptions
from concurrent.futures import thread
from datetime import datetime
from unittest import result
from django.forms import ValidationError
from rest_framework import response,status
from rest_framework import viewsets,views,permissions
from .models import Infodoctor
from info import models as pmodels
from . import serializers
from role_manager.permissions import HasGroupRolePermission
class Companyviewset(viewsets.ModelViewSet):
    queryset = Infodoctor.objects.all()
    serializer_class=serializers.CompanySerializer
    permission_classes=[permissions.IsAuthenticated, HasGroupRolePermission]
    def create(self, request, *args, **kwargs):
        data =request.data
        user={}
        user['first_name']=data.get('first_name')
        user['last_name']=data.get('last_name')
        user['phone']=data.get('moble_phone')[0]
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
