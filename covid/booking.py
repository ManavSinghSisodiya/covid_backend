from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view


from .models import Booking

from .serializers import BookingSerializer



@api_view(['GET', 'POST', 'DELETE'])
def Submit_booking(request):
  
 try:
   if request.method=='POST':
    book_serializer=BookingSerializer(data=request.data)
    # print(book_serializer,book_serializer.is_valid(),request.data)
    if(book_serializer.is_valid()):
    
      book_serializer.save()
      return JsonResponse({"message":'Slot booked Successfully',"status":True},safe=False)
    else:
      return JsonResponse({"message":'Fail to Book',"status":False},safe=False) 
 except Exception as e:
    print("Error submit:",e)
    return JsonResponse({"message":'Fail ',"status":False},safe=False) 
 