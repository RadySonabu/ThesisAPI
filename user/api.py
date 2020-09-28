from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

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


class UserRetrieveAPI(generics.RetrieveAPIView):
    """ User Retrieval API """
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
        return Response(serializer.data)

class UserLogoutAPI(generics.GenericAPIView):
    """ User Logout API """
    serializer_class = UserLoginSerializer

