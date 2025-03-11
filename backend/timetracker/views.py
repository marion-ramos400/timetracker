from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import json

from .serializers import UserSerializer, TaskSerializer
from .models import Task

class Ping(APIView):
    def get(self, request):
        return Response(data="OK", status=200)

class SignUp(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer

class CreateTask(APIView):
    def post(self, request):
        reqdata = request.data
        username = reqdata.get("user")
        usermodel = get_user_model() 
        user = usermodel.objects.filter(username=username).first()
        if user:
            serdata = {
                "user": user.id,
                "start_dt": reqdata["start_dt"],
                "hours": reqdata["hours"],
                "description": reqdata["description"],
                "project": reqdata["project"]
            }
            ser = TaskSerializer(data=serdata)
            if ser.is_valid(raise_exception=True):
                ser.save()
                return JsonResponse(ser.data, status=201)
            return JsonResponse(ser.errors, status=400)
        return JsonResponse(
            {"error": f"username {username} not found"},
            status=404
        )

    #model = Task
    #serializer_class = TaskSerializer