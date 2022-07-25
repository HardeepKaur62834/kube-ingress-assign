from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from . models import Employee
from rest_framework.views import APIView
from . Serializers import EmployeeSerializer
from rest_framework.response import Response
# Create your views here.

class EmployeeView(APIView):

    def get(self, request):
        emp_data = Employee.objects.all()
        print(emp_data)
        serializer = EmployeeSerializer(emp_data,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        emp_data = request.data
        print(emp_data)
        new_emp = Employee.objects.create(emp_first_name= emp_data["emp_first_name"],emp_last_name=emp_data["emp_last_name"],eid=emp_data["eid"])
        new_emp.save()
        serializer = EmployeeSerializer(new_emp)
        return Response(serializer.data)