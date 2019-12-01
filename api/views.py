from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework import authentication, permissions

from django.contrib.auth import authenticate

from .serializers import UserSerializer, DoctorSerializer, UserProfileSerializer

from database.models import Pacjent
from database.models import CustomUser
import logging

logger = logging.getLogger(__name__)
# Create your views here.


class ApiRootView(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'create_user': reverse(UserCreateView.name, request=request),
                'user_login': reverse(GetAuthTokenView.name, request=request),
                'create_doctor': reverse(DoctorCreateView.name, request=request),
                'user_profile': reverse(UserEditProfileView.name, request=request),
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

    def get(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous is False and user.fk_id_pacjent is not None:
            profile = Pacjent.objects.get(id=user.fk_id_pacjent.id)
            return Response({
                'name': profile.name,
                'surname': profile.surname,
                'pesel': profile.pesel,
                'ulica': profile.ulica,
                'nr_ulicy': profile.nr_ulicy,
                'nr_mieszkania': profile.nr_mieszkania,
                'kod_pocztowy': profile.kod_pocztowy,
                'miasto': profile.miasto,
                'wojewodztwo': profile.wojewodztwo,
                'telefon': profile.telefon,
                'dokumenty': profile.dokumenty,
            })
        else:
            return Response(status.HTTP_401_UNAUTHORIZED)

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
            return Response(status.HTTP_401_UNAUTHORIZED)


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
