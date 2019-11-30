from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreate, ApiRoot, GetAuthToken

urlpatterns = [
    path('create_user/', UserCreate.as_view(), name=UserCreate.name),
    url(r'^$', ApiRoot.as_view(), name=ApiRoot.name),
    url(r'^login_user/', GetAuthToken.as_view(), name=GetAuthToken.name),
]
