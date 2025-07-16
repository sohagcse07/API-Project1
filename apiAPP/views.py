from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# apiAPP এর model এবং serializer import করা হয়েছে
from apiAPP.models import Company , Employe
from apiAPP.serializers import CompanySerializer , EmployeeSerializers

# এই view function টি home page রেন্ডার করার জন্য
def home_page(request):
    # home.html template রেন্ডার করে রিটার্ন করছে
    return render(request, 'home.html')

# Company এর জন্য একটি ModelViewSet তৈরি করা হয়েছে
class CompanyViewset(viewsets.ModelViewSet):
    # সমস্ত Company object এর queryset সেট করা হয়েছে
    queryset = Company.objects.all()
    # কোন serializer ব্যবহার হবে তা সেট করা হয়েছে
    serializer_class = CompanySerializer

    #detail=True মানে এটা একটা নির্দিষ্ট object এর জন্য route banabe (মানে /company/1/employess/ এর মত)
    #methods=["get"] মানে এটা GET request handle korbe।
    @action ( detail=True , methods= ["get"])
    def employess ( self , request , pk = None): 
        
        #pk প্যারামিটারটা company object er id — তুমি এটা দিয়ে specific company খুঁজে পাচ্ছো।
        company = Company.objects.get( pk = pk )#নির্দিষ্ট ID দিয়ে company বের করছো।
        
        # ওই company'r অধীনে জতো employee আছে, সব বের করছো।
        emps = Employe.objects.filter( company = company)
        
        # multiple employee object serialize করছো। json e convert korteci serializer diya
        emps_serializer = EmployeeSerializers ( emps , many = True , context = { "request" : request})

        return Response ( emps_serializer.data)

class EmployeViewset ( viewsets.ModelViewSet):

    queryset = Employe.objects.all()

    serializer_class = EmployeeSerializers