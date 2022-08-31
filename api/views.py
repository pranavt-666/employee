from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.models import Employees
from api.serializer import EmployeeSerializer


class EmployeeView(ViewSet):
    def list(self, request, *args, **kwargs):
        qs = Employees.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def retrieve(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = Employees.objects.get(id=id)
        serializer = EmployeeSerializer(qs)
        return Response(data=serializer.data)
        
    def update(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        instance = Employees.objects.get(id=id)
        serializer = EmployeeSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        instance = Employees.objects.get(id=id)
        instance.delete()
        return Response({'msg':'deleted'})

    