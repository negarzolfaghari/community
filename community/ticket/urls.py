from django.urls import path,include,re_path
from rest_framework import routers
from ticket import api



router=routers.DefaultRouter()
router.register(r'Thread',api.Threadviewset)
router.register(r'Message',api.Messageviewset)
urlpatterns=[
    path('',include(router.urls)),

    # path ('list/',api.Personviewset),
]
