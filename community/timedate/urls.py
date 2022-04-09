from django.urls import path,include,re_path
from rest_framework import routers
from timedate import api



router=routers.DefaultRouter()
router.register(r'taketime',api.Taketimeviewset)
urlpatterns=[
    path('list_time/',api.ListTimeAPIView.as_view()),
    path('select_time/',api.SelectApiView.as_view()),
    path('',include(router.urls)),
    

    # path ('list/',api.Personviewset),
]
