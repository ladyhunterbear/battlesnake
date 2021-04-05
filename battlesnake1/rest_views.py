from django.shortcuts import render
from rest_framework.generics import GenericAPIView
#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from rest_framework import permissions
from battlesnake1.serializers import UserSerializer, GroupSerializer


class RegisterView(GenericAPIView):
    def post(self, request):
        pass