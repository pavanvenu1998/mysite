from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . models import products
from . serializers import employeesSerializer
from . serializers import productsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class employeeList(APIView):
    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1,many=True)
        return Response(serializer.data)

class productList(APIView):
    def get(self,request):
        products1=products.objects.all()
        serializer=productsSerializer(products1,many=True)
        return Response(serializer.data)

    def post(self):
        pass

    def post(self):
        pass

