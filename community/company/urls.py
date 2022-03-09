
from django.urls import path,include,re_path
from rest_framework import routers
from . import api



router=routers.DefaultRouter()
router.register(r'company',api.Companyviewset)
urlpatterns=[
    path ('report/',api.ReportApiView.as_view()),
    path('',include(router.urls)),
    
]
