from django.conf.urls import url, include
from django.urls import path
from rest_framework.authtoken import views
from .views import UserCreateView, UserListView, ApiRootView, DoctorListView, PrzychodniaCreateView, GetAuthTokenView, DoctorCreateView, UserEditProfileView, DoctorEditProfileView, PrzychodniaListView
from .views import WizytaCreateView, WizytaListView, GetCustomUserDataView, ObjawyListView, WizytaDetailView, EpidemicDetailView, FIleUploadView

urlpatterns = [
    path('create/user/', UserCreateView.as_view(), name=UserCreateView.name),
    path('create/doctor/', DoctorCreateView.as_view(), name=DoctorCreateView.name),
    path('create/przychodnia/', PrzychodniaCreateView.as_view(), name=PrzychodniaCreateView.name),
    path('wizyta/create/', WizytaCreateView.as_view(), name=WizytaCreateView.name),
    path('wizyta/details/<int:pk>/', WizytaDetailView.as_view(), name=WizytaDetailView.name),
    path('wizyta/epidemic/<int:pk>/', EpidemicDetailView.as_view(), name=EpidemicDetailView.name),
    path('wizyta/patchFile/<int:pk>/', FIleUploadView.as_view(), name=FIleUploadView.name),
    path('przychodnia/list/', PrzychodniaListView.as_view(), name=PrzychodniaListView.name),
    path('user/main_profile/', GetCustomUserDataView.as_view(), name=GetCustomUserDataView.name),
    path('users/patient/profile/', UserEditProfileView.as_view(), name=UserEditProfileView.name),
    path('users/patient/list/', UserListView.as_view(), name=UserListView.name),
    path('users/wizyty/', WizytaListView.as_view(), name=WizytaListView.name),
    path('users/doctor/profile/', DoctorEditProfileView.as_view(), name=DoctorEditProfileView.name),
    path('users/doctor/list/', DoctorListView.as_view(), name=DoctorListView.name),
    path('objawy/list/', ObjawyListView.as_view(), name=ObjawyListView.name),
    url(r'^$', ApiRootView.as_view(), name=ApiRootView.name),
    url(r'^login_user/', GetAuthTokenView.as_view(), name=GetAuthTokenView.name),
    url(r'^api-auth/', include('rest_framework.urls')),
]
