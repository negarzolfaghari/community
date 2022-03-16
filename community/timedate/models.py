from django.db import models
from django.conf import settings


# Create your models here.
class TakeTime(models.Model):
    SHANBE='SHANBE'
    YEKSHANBE='YEKSHANBE'
    DOSHANBE='DOSHANBE'
    SESHANBE='SESHANBE'
    CHARSHANBE='CHARSHANBE'
    PANSHANBE='PANSHANBE'
    TYPE_DAY=(( SHANBE,'SHANBE'),(YEKSHANBE,'YEKSHANBE'),(DOSHANBE,'DOSHANBE'),(SESHANBE,'SESHANBE'),( CHARSHANBE,'CHARSHANBE'),(PANSHANBE,'PANSHANBE'))
    T1='8-9'
    T2='9-10'
    T3='10-11'
    T4='11-12'
    T5='15-16'
    T6='16-17'
    T7='17-18'
    TYPE_TIME=((T1,T1),(T2,T2),(T3,T3),(T4,T4),(T5,T5),(T6,T6),(T7,T7))

    date =models.DateField()
    day =models.CharField(max_length=50,null=True,blank=True)
    time =models.CharField(max_length=50,choices=TYPE_TIME)
    user1 =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='taketime_user',null=True,blank=True)
    is_active =models.BooleanField(default=True)
    moorningOrafter =models.BooleanField(default=True)
