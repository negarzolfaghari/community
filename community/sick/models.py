from django.db import models
from django.conf import settings

# Create your models here.
class Infosick(models.Model):
    MALE='MALE'
    FEMALE='FEMALE'
    GENDER_TYPE=((MALE,'MALE'),(FEMALE,'FEMALE'))
#FIELD
    created =models.DateTimeField(auto_now_add=True,editable=False,null=True)
    last_updated =models.DateTimeField(auto_now=True,editable=False,null=True)
    first_name =models.CharField(max_length=500)
    last_name =models.CharField(max_length=50)
    gender =models.CharField(max_length=6,choices=GENDER_TYPE)
    national_code =models.CharField(max_length=50)
    mobile_phone =models.CharField(max_length=11)
    email =models.EmailField()
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='infosick_user',null=True,blank=True)


def __str__(self):
    return f"{self.first_name},{self.last_name},{self.national_code}"
    
