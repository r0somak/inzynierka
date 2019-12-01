from django.conf.urls import url, include
from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreateView, ApiRootView, GetAuthTokenView, DoctorCreateView, UserEditProfileView, DoctorEditProfileView


urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name=UserCreateView.name),
    path('create_doctor/', DoctorCreateView.as_view(), name=DoctorCreateView.name),
    path('users/patient/profile/', UserEditProfileView.as_view(), name=UserEditProfileView.name),
    path('users/doctor/profile/', DoctorEditProfileView.as_view(), name=DoctorEditProfileView.name),
    url(r'^$', ApiRootView.as_view(), name=ApiRootView.name),
    url(r'^login_user/', GetAuthTokenView.as_view(), name=GetAuthTokenView.name),
    url(r'^api-auth/', include('rest_framework.urls')),
]
