from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
import json
from datetime import timedelta

from .serializers import UserSerializer, TaskSerializer
from .models import Task
from .utils import (
    retrieve_user,
    get_datetime_range,
)
from .projects import projects

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
    def get(self, request):
        reqdata = request.query_params
        month = reqdata.get("month")
        week = reqdata.get("week")
        username = reqdata.get("user")
        #add validation for month, week, and username
        #user = retrieve_user(username)
        #if user:

        startdt, enddt = get_datetime_range(month, week)
        out = {
            "tasks":[], 
            "project_totals": {},
            "week_start_dt": str(startdt),
            "week_end_dt": str(enddt - timedelta(days=1)),
        } 
        for p in projects:
            out["project_totals"][p] = 0
        tasks = Task.objects.filter(start_dt__range=(startdt, enddt))
        for t in tasks:
            tdata = TaskSerializer(t).data
            tdata["user"] = retrieve_user(userid=tdata["user"]).username
            out["tasks"].append(tdata)
            out["project_totals"][t.project] += tdata["hours"]
        return JsonResponse(
            data=out,
            status=200
        )
        
            