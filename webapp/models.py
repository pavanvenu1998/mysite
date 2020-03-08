from django.db import models
from django.conf import settings


class employees(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    emp_id=models.IntegerField()


class products(models.Model):
    productname=models.CharField(max_length=30)
    product_id=models.IntegerField()



    def __str__(self):
        return self.firstname

    def __str__(self):
        return self.productname
