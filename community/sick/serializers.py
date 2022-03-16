from . import models
# from drf_extra_fields.geo_fields import PointField
from auth_rest_phone.serializers import UserCreatePasswordRetypeSerializer 
from drf_writable_nested.serializers import WritableNestedModelSerializer 

class SickSerializer(WritableNestedModelSerializer):
    # locations=PointField()
    user=UserCreatePasswordRetypeSerializer()
    class Meta:
        model =models.Infosick
        fields =['pk','first_name', 'last_name', 'gender', 'national_code', 'mobile_phone', 'email', 'user']