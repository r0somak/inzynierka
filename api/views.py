from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from rest_framework import status

from django.contrib.auth import authenticate

from .serializers import UserSerializer

from database.models import CustomUser


# Create your views here.


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response(
            {
                'create_user': reverse(UserCreate.name, request=request),
                'user_login': reverse(GetAuthToken.name, request=request),
            }
        )


class UserCreate(generics.CreateAPIView):
    name = 'create-user'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class GetAuthToken(APIView):
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
