from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from apiAPP import views 
from apiAPP.views import CompanyViewset , EmployeViewset

router = DefaultRouter()

router.register('companies' ,CompanyViewset ) # url hit korbe companies diya

router.register("Employess" , EmployeViewset)



urlpatterns = [
    
    path( 'home' , views.home_page , name="home"  ),
    path( '' , include(router.urls)  ),
]