from . import models
# from drf_extra_fields.geo_fields import PointField
from auth_rest_phone.serializers import UserCreatePasswordRetypeSerializer 
from drf_writable_nested.serializers import WritableNestedModelSerializer 

class DoctorSerializer(WritableNestedModelSerializer):
    # locations=PointField()
    user=UserCreatePasswordRetypeSerializer()
    class Meta:
        model =models.Infodoctor
        fields =['pk','first_name', 'last_name', 'gender', 'dr_code', 'mobile_phone', 'email', 'user', 'expertise']
class ExpertiseSerializer(WritableNestedModelSerializer):
    # locations=PointField()
    user=UserCreatePasswordRetypeSerializer()
    class Meta:
        model =models.Expertise
        fields =['pk','expertise']       