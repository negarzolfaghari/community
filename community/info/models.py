from django.db import models
from django.contrib.gis.db import models as models
from django.conf import settings
# Create your models here.
class Person (models.Model):
    MALE='male'
    FEMALE='female'
    GENDER_TYPE=((MALE,'male'),(FEMALE,'female'))
    BISAVAD='bisavad'
    SICL='sicl'
    DIPLOM='diplom'
    KARDANI='kardani'
    KARSHENASI='karshenasi'
    KARSHENASIARSHAD='karshenasiarshad'
    DOCTORA='doctora'
    EDUCATION_TYPE=((BISAVAD,'bisavad'),(SICL,'sicl'),(DIPLOM,'diplom'),(KARDANI,'kardani'),(KARSHENASI,'karshenasi'),(KARSHENASIARSHAD,'karshenasiarshad'),(DOCTORA,'doctora'))
    PERSONAL='PERSONAL'
    RENT='rent'
    OWNERSHIP_TYPE=((PERSONAL,'PERSONAL'),(RENT,'rent'))


    #fields
    created =models.DateTimeField(auto_now_add=True,editable=False)
    last_updated =models.DateTimeField(auto_now=True,editable=False)
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    gender =models.CharField(max_length=6,choices=GENDER_TYPE)
    father_name =models.CharField(max_length=50)
    birth_place =models.CharField(max_length=50)
    place_issuance_identitycard =models.CharField(max_length=50)
    birth_date =models.DateField()
    identity_number =models.CharField(max_length=1000)
    identity_serial_number =models.CharField(max_length=1000)
    national_code =models.CharField(max_length=100)
    education =models.CharField(max_length=100,choices=EDUCATION_TYPE)
    job =models.CharField(max_length=100)
    work_address =models.CharField(max_length=1000)
    locations =models.PointField(null=True,blank=True)
    home_address =models.CharField(max_length=100)
    mobile_number =models.CharField(max_length=11)
    phone_number =models.CharField(max_length=10)
    aviculter_address =models.CharField(max_length=1000)
    postalcode =models.CharField(max_length=100)
    township =models.CharField(max_length=100)
    user =models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='person_user',null=True,blank=True)
    
    #relationship
    company =models.ForeignKey('company.Company',on_delete=models.CASCADE,related_name='person_company',null=True,blank=True)




class Meta:
    ordering=('-created',)

def __str__(self):
    return f"{self.first_name},{self.last_name},{self.national_code}"



















    
