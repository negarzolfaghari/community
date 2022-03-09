from . import models
from drf_extra_fields.geo_fields import PointField
from auth_rest_phone.serializers import UserCreatePasswordRetypeSerializer 
from drf_writable_nested.serializers import WritableNestedModelSerializer 
class CompanySerializer(WritableNestedModelSerializer):
    locations=PointField()
    user=UserCreatePasswordRetypeSerializer()
    class Meta:
        model =models.Company
        fields =['pk','website',
    'username','national_code','national_code','email','last_name','date_completion','first_name','created', 'last_updated', 'name', 'phone','user', 'address_company', 'locations', 'locationtype']