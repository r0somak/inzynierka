from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

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
            }
        )


class UserCreate(generics.CreateAPIView):
    name = 'create-user'
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
