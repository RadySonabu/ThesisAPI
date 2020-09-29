from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import MyUser
from .serializers import (
    UserInputSerializer, 
    UserOutputSerializer, 
    UserLoginSerializer
)

class UserCreateAPI(generics.CreateAPIView):
    """ User creation API """
    queryset = MyUser.objects.all()
    serializer_class = UserInputSerializer


class UserListAPI(generics.ListAPIView):
    """ User List API """
    queryset = MyUser.objects.all()
    serializer_class = UserOutputSerializer

class UserRetrieveAPI(generics.RetrieveAPIView):
    """ User Retrieve API """
    queryset = MyUser.objects.all()
    serializer_class = UserOutputSerializer

class UserUpdateAPI(generics.UpdateAPIView):
    """ User Update API """
    queryset = MyUser.objects.all()
    serializer_class = UserInputSerializer


class UserDestroyAPI(generics.DestroyAPIView):
    """ User Deletion API """
    queryset = MyUser.objects.all()
    serializer_class = UserOutputSerializer


class UserLoginAPI(generics.GenericAPIView):
    """ User Login API """
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        access_token = AccessToken.for_user(user)

        token = {'token': str(access_token)}
        return Response(token)

class UserLogoutAPI(generics.GenericAPIView):
    """ User Logout API """
    serializer_class = UserLoginSerializer

    def get(self, request):

        try:
            response = HttpResponse("hello")
            response.delete_cookie('token')
        except Exception:
            response = None

        return response