from rest_framework import response,status


from rest_framework import viewsets,views
from .models import Person
from . import serializers
class Personviewset(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class=serializers.PersonSerializer
    # permission_classes=((IsSuperUserOrReadOnly,))
    def create(self, request, *args, **kwargs):
        data =dict(request.data)
        data['user']=request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


        
