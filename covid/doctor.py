from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render

from .models import States
from .models import City
from .models import Doctors
from .serializers import DoctorSerializer,CitySerializer,StateSerializer

from rest_framework.decorators import api_view


@api_view(["GET","POST","DELETE"])
def Submit_User(request):
    try:
        if request.method=="POST":
            user_serializer=DoctorSerializer(data=request.data)
                # print(doctor_serializer,doctor_serializer.is_valid(),request.data)

            if(user_serializer.is_valid()):
                user_serializer.save()
                return JsonResponse({"message":'sucess',"status":True},safe=False)
            else:
                return JsonResponse({"message":'fail to submit',"status":False},safe=False)
    except Exception as e:
        print('error submit: ',e)
        return JsonResponse({"message":'fail to submit',"status":False},safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def Doctor_Login(request):
  if request.method=='POST':
  
    email=request.data['emailid']
    pwd=request.data['password']
    doctor=Doctors.objects.all().filter(emailid=email,password=pwd)
     
    doctor_serializer = DoctorSerializer(doctor,many=True)
    if(len(doctor_serializer.data)==1):
     return JsonResponse({"data":doctor_serializer.data,"status":True },safe=False)
    else:
     return JsonResponse({"data":[],"status":False },safe=False)  
       
  return JsonResponse({"data":{},"status":False },safe=False) 
   