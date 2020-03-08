
from django.urls import path
from webapp import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
     path('admin/', admin.site.urls),
     path('employees/', views.employeeList.as_view()),
     path('products/', views.productList.as_view()),

]
