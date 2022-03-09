from django.db import models
from django.contrib.gis.db import models as models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
 

# Create your models here.
class Company (models.Model):
    MAINSTREET ='MAINSTREET'
    AUXILIARYROAD ='AUXILIARYROAD'
    LOCATIONS_TYPE =((MAINSTREET,'MAINSTREET'),(AUXILIARYROAD,'AUXILIARYROAD'))
    #field
    date_completion =models.DateField(null=True)
    name =models.CharField(max_length=50,null=True)
    created =models.DateTimeField(auto_now_add=True,editable=False)
    last_updated =models.DateTimeField(auto_now=True,editable=False)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email =models.EmailField(max_length=100,null=True)
    national_code =models.CharField(max_length=12,null=True)
    active =models.BooleanField(default=True,null=True)
    website =models.URLField(null=True,blank=True)
    username =models.CharField(max_length=50,null=True)
    phone =ArrayField(models.CharField(max_length=12))
    address_company =models.TextField()
    locations =models.PointField(null=True,blank=True)
    locationtype =models.CharField(max_length=50,choices=LOCATIONS_TYPE)
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='company_user',null=True,blank=True)

    #relations


class Meta:
    ordering=('-created',)

def __str__(self):
    return f"{self.pk},{self.name}" 



    
       