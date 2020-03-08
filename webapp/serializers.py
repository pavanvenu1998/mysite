from rest_framework import serializers
from . models import employees
from . models import products

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields="__all__"

class productsSerializer(serializers.ModelSerializer):

    class Meta:
        model=products
        fields="__all__"
