from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class Ping(APIView):
    def get(self, request):
        return Response(data="OK", status=200)

