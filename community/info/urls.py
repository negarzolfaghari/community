
from django.urls import path,include,re_path
from rest_framework import routers
from . import api



router=routers.DefaultRouter()
router.register(r'Person',api.Personviewset)
urlpatterns=[
    path('',include(router.urls)),
    # path ('list/',api.Personviewset),
]
