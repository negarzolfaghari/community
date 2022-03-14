from django.urls import re_path as url

from auth_rest_phone.social import views

urlpatterns = [
    url(
        r"^o/(?P<provider>\S+)/$",
        views.ProviderAuthView.as_view(),
        name="provider-auth",
    )
]
