from rest_framework import serializers
from .models import TakeTime

class TaketimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=TakeTime
        fields=['pk','date','day','time','user1','is_active','moorningOrafter']
