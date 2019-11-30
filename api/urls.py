from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreate, ApiRoot

urlpatterns = [
    path('create_user/', UserCreate.as_view(), name=UserCreate.name),
    url(r'^$', ApiRoot.as_view(), name=ApiRoot.name),
]