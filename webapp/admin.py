from django.contrib import admin

from . models import employees
from . models import products

admin.site.register(employees)
admin.site.register(products)

