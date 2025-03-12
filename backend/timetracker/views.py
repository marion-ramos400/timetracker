from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
import json
from datetime import timedelta

from .serializers import UserSerializer, TaskSerializer
from .receivers import *
from .models import Task
from .utils import (
    retrieve_user,
    get_datetime_range,
    get_users_list,
)
from .projects import projects

class Ping(APIView):
    def get(self, request):
        return Response(data="OK", status=200)

class SignUp(APIView):
    def post(self, request):
        reqdata = request.data
        serdata = {
            "username": reqdata.get("username"),
            "password": reqdata.get("password")
        }

        ser = UserSerializer(data=serdata)
        if ser.is_valid(raise_exception=True):
            userobj = ser.save()
            out = ser.data.copy()
            out["token"] = str(Token.objects.get(user=userobj))
            return JsonResponse(out, status=201)
    #model = get_user_model()
    #serializer_class = UserSerializer

class LogIn(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        check = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            'token': str(Token.objects.get(user=request.user))
        }
        return Response(check)


class CreateTask(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        reqdata = request.data
        username = reqdata.get("user")
        user = retrieve_user(username)
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

class GetTasks(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reqdata = request.query_params
        month = reqdata.get("month")
        week = reqdata.get("week")
        username = reqdata.get("user")
        user = None
        if not username:
            #get user from token auth
            token_h = request.headers.get("Authorization") 
            if token_h:
                token_h = token_h.split()[1]
                user = Token.objects.get(key=token_h).user
                print(user)
        else:
            user = retrieve_user(username=username)

        startdt, enddt = get_datetime_range(month, week)
        out = {
            "month": month,
            "week": week,
            "week_start_dt": str(startdt),
            "week_end_dt": str(enddt - timedelta(days=1)),
            "tasks":[], 
            "projects_total_hrs": {},
        }
        for p in projects:
            out["projects_total_hrs"][p] = 0
        tasks = Task.objects.filter(start_dt__range=(startdt, enddt), user=user).order_by('start_dt')
        for t in tasks:
            tdata = TaskSerializer(t).data
            tdata["user"] = retrieve_user(userid=tdata["user"]).username
            out["tasks"].append(tdata)
            out["projects_total_hrs"][t.project] += tdata["hours"]
        return JsonResponse(
            data=out,
            status=200
        )

class GetUsers(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        token_h = request.headers.get("Authorization") 
        if token_h:
            token_h = token_h.split()[1]
            requesting_user = Token.objects.get(key=token_h).user
        
        users_list = get_users_list(requesting_user)
        return JsonResponse(
            data={"users": users_list},
            status=200
        )