from django.urls import re_path as url

from auth_rest_phone import views

urlpatterns = [
    url(r"^token/login/?$", views.TokenCreateView.as_view(), name="login"),
    url(r"^token/logout/?$", views.TokenDestroyView.as_view(), name="logout"),
]
