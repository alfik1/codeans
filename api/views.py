from django.shortcuts import render
from api.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import permissions,authentication
# Create your views here.

class UserView(ViewSet):
    def create(self, request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

