from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category
from .models import States
from .models import City
from .models import Doctors
from .models import Patient
from .models import Booking

class CategorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Category
        fields = "__all__"
class StateSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = States
        fields = "__all__"
class CitySerializer(serializers.ModelSerializer):        
    class Meta:
        model = City
        fields = "__all__"    
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
       
        model = Doctors
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields="__all__"

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']

# class VaccinationCenterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = VaccinationCenter
#         fields = '__all__'

# class VaccinationSlotSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = VaccinationSlot
#         fields = '__all__'