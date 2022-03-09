from django.urls import path,include,re_path
from rest_framework import routers
from timedate import api



router=routers.DefaultRouter()
router.register(r'taketime',api.Taketimeviewset)
urlpatterns=[
    path('',include(router.urls)),

    # path ('list/',api.Personviewset),
]
