from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import json

from .serializers import UserSerializer

class Ping(APIView):
    def get(self, request):
        return Response(data="OK", status=200)

class SignUp(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer