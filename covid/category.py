from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from  .models import Category
from  .serializers import CategorySerializer

from  .models import States
from  .models import City
from  .serializers import StateSerializer
from  .serializers import CitySerializer

from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def Category_List(request):
 if request.method=='GET':
    categorylist=Category.objects.all() 
    category_serializer = CategorySerializer(categorylist,many=True)
    return JsonResponse(category_serializer.data,safe=False)
 return JsonResponse({},safe=False) 


@api_view(["GET","POST","DELETE"])
def add_center(request):
    try:
        if request.method=="POST":
            Center_serializer=CategorySerializer(data=request.data)
                # print(doctor_serializer,doctor_serializer.is_valid(),request.data)

            if(Center_serializer.is_valid()):
                Center_serializer.save()
                return JsonResponse({"message":'sucess',"status":True},safe=False)
            else:
                return JsonResponse({"message":'fail to submit',"status":False},safe=False)
    except Exception as e:
        print('error submit: ',e)
        return JsonResponse({"message":'fail to submit',"status":False},safe=False)


@api_view(['GET', 'POST', 'DELETE'])
def center_List(request):
  if request.method=='POST':
  
    id=request.data['id']
    
    centerlist=Category.objects.all().filter(city_id=id)
     
    center_serializer = CategorySerializer(centerlist,many=True)
  
    return JsonResponse(center_serializer.data,safe=False)
  return JsonResponse({},safe=False) 