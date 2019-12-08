from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework import filters

from django.contrib.auth import authenticate
from django.db import IntegrityError

from .serializers import UserSerializer, DoctorSerializer, UserProfileSerializer, DoctorProfileSerializer, PrzychodniaSerializer, WizytaSerializer

from database.models import Pacjent, Lekarz, Przychodnia, Wizyta
from database.models import CustomUser
import logging

logger = logging.getLogger(__name__)
# Create your views here.


class ApiRootView(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'TWORZENIE': 'ENDPOINTY DO TWORZENIA OBIEKTOW',
                'create_patient': reverse(UserCreateView.name, request=request),
                'create_przychodnia': reverse(PrzychodniaCreateView.name, request=request),
                'create_doctor': reverse(DoctorCreateView.name, request=request),
                'create_wizyta': reverse(WizytaCreateView.name, request=request),
                'AUTHTOKEN': 'ENDPOINT DO UZYSKANIA AUTHTOKEN',
                'user_login': reverse(GetAuthTokenView.name, request=request),
                'EDYCJA PROFILU': 'ENDPOINTY DO EDYCJI PROFILU',
                'user_profile': reverse(UserEditProfileView.name, request=request),
                'doctor_profile': reverse(DoctorEditProfileView.name, request=request),
                'LISTA': 'ENDPOINTY DO UZYSKANIA LISTY WSZYSTKICH OBIEKTÓW DANEGO TYPU',
                'user_list': reverse(UserListView.name, request=request),
                'doctor_list': reverse(DoctorListView.name, request=request),
                'przychodnia_list': reverse(PrzychodniaListView.name, request=request),
                'wizyta_list': reverse(WizytaListView.name, request=request),
            }
        )


class UserCreateView(generics.CreateAPIView):
    name = 'create-user'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserEditProfileView(generics.RetrieveUpdateAPIView):
    name = 'user-edit-profile'
    serializer_class = UserProfileSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is False and user.fk_id_pacjent is not None:
            profile = Pacjent.objects.get(id=user.fk_id_pacjent.id)
            serializer = UserProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is False and user.fk_id_pacjent is not None:
            profile = Pacjent.objects.get(id=user.fk_id_pacjent.id)
            serializer = UserProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_403_FORBIDDEN)


class GetAuthTokenView(APIView):
    name = 'user-login'
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({
                'token': user.auth_token.key
            })
        else:
            return Response({
                'error': "Wrong Credentials"
            }, status=status.HTTP_400_BAD_REQUEST)


class DoctorCreateView(generics.CreateAPIView):
    name = 'create-doctor'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = DoctorSerializer


class DoctorEditProfileView(generics.RetrieveUpdateAPIView):
    name = 'doctor-edit-profile'
    serializer_class = DoctorProfileSerializer
    permission_classes = (IsAuthenticated,)

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is False and user.fk_id_lekarz is not None:
            profile = Lekarz.objects.get(id=user.fk_id_lekarz.id)
            serializer = DoctorProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is False and user.fk_id_lekarz is not None:
            profile = Lekarz.objects.get(id=user.fk_id_lekarz.id)
            serializer = DoctorProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_403_FORBIDDEN)


class PrzychodniaCreateView(generics.CreateAPIView):
    name = 'create-przychodnia'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = PrzychodniaSerializer
    permission_classes = (IsAuthenticated,)


class DoctorListView(generics.ListAPIView):
    name = 'doctor-list'
    queryset = Lekarz.objects.all()
    serializer_class = DoctorProfileSerializer
    permission_classes = (IsAuthenticated,)


class UserListView(generics.ListAPIView):
    name = 'user-list'
    queryset = Pacjent.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class PrzychodniaListView(generics.ListAPIView):
    name = 'przychodnia-list'
    queryset = Przychodnia.objects.all()
    serializer_class = PrzychodniaSerializer
    permission_classes = (IsAuthenticated,)


class WizytaCreateView(generics.CreateAPIView):
    name = 'create-wizyta'
    serializer_class = WizytaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is False and user.fk_id_pacjent is not None:
            serializer = WizytaSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    serializer.save(fk_id_pacjent=user.fk_id_pacjent)
                except IntegrityError as e:
                    return Response(status.HTTP_400_BAD_REQUEST)
                return Response(serializer.data)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_403_FORBIDDEN)

    # def perform_create(self, serializer):
    #     if self.request.user.is_anonymous is False and self.request.user.fk_id_pacjent is not None:
    #         serializer.save(
    #             fk_id_pacjent=self.request.user.fk_id_pacjent
    #         )
    #     else:
    #         return Response(status.HTTP_401_UNAUTHORIZED)


class WizytaListView(generics.ListAPIView):
    name = 'wizyta-list'
    serializer_class = WizytaSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['data_wizyty']
    search_fields = [u'data_wizyty', u'fk_id_lekarz__name', u'fk_id_lekarz__surname']
    # def get(self, request, *args, **kwargs):
    #     user = request.user
    #     if user.is_anonymous is False:
    #         if user.fk_id_pacjent is not None:
    #             pacjent = Pacjent.objects.filter(id=user.fk_id_pacjent.id)
    #             serializer = WizytaSerializer(pacjent, data=request.data)
    #             if serializer.is_valid():
    #                 return Response(serializer.data)
    #             else:
    #                 return Response(status.HTTP_400_BAD_REQUEST)
    #         elif user.fk_id_lekarz is not None:
    #             pass
    #         else:
    #             pass
    #     else:
    #         return Response(status.HTTP_403_FORBIDDEN)

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous is False:
            if user.fk_id_pacjent is not None:
                queryset = Wizyta.objects.filter(fk_id_pacjent=user.fk_id_pacjent)
                return queryset
            elif user.fk_id_lekarz is not None:
                queryset = Wizyta.objects.filter(fk_id_lekarz=user.fk_id_lekarz)
                return queryset
            else:
                pass

