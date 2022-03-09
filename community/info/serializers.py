from rest_framework import serializers
from info.models import Person
from drf_extra_fields.geo_fields import PointField
class PersonSerializer(serializers.ModelSerializer):
    locations=PointField()
    class Meta:
        model =Person
        fields =["pk",'created','company', 'last_updated', 'first_name', 'last_name','user' ,'gender', 'father_name', 'birth_place', 'place_issuance_identitycard', 'birth_date', 'identity_number', 'identity_serial_number', 'national_code', 'education', 'job', 'work_address', 'phone_number', 'postalcode', 'township','locations' ]