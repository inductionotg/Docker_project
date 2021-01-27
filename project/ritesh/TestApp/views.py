from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics  import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from TestApp.models import *
from TestApp.serializers import * 
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'