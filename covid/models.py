from django.db import models

# Create your models here.


class States(models.Model):
    statename = models.CharField(max_length=100, blank=False, default='')

class City(models.Model):
    states = models.ForeignKey(States, on_delete=models.CASCADE)
   
    cityname = models.CharField(max_length=100, blank=False, default='')

class Category(models.Model):
    city=models.ForeignKey(City, on_delete=models.CASCADE)
 
    categoryname = models.CharField(max_length=100, blank=False, default='')
    # time= models.CharField(max_length=250,blank=False, default='')
    # icon = models.CharField(max_length=200,blank=False, default='')

# class Time(models.Model):
#     category=models.ForeignKey()

class Doctors(models.Model):
    
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=False, default='')
     
    gender = models.CharField(max_length=10, blank=False, default='')
    dob = models.CharField(max_length=25, blank=False, default='')
    address = models.CharField(max_length=150, blank=False, default='')
    states = models.ForeignKey(States, on_delete=models.CASCADE,related_name="state")
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    emailid = models.CharField(max_length=100, blank=False, default='')
    mobileno = models.CharField(max_length=100, blank=False, default='')
    password = models.CharField(max_length=100, blank=False, default='')
    photograph = models.ImageField(upload_to='static/')

class Patient(models.Model):
    username=models.CharField(max_length=200,blank=False,default='')
    city=models.CharField(max_length=200,blank=False,default='')
    emailid=models.CharField(max_length=200,primary_key=True)
    dob=models.CharField(max_length=200,blank=False,default='')
    mobileno=models.CharField(max_length=200,blank=False,default='')
    password=models.CharField(max_length=200,blank=False,default='') 

class Booking(models.Model):
    patientname=models.CharField(max_length=200)
    age=models.CharField(max_length=100)
    dose=models.CharField(max_length=100)
    cost=models.CharField(max_length=100)
    vaccine=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100)
    date=models.CharField(max_length=200,blank=False,default='')

    
    state=models.ForeignKey(States,on_delete=models.CASCADE)
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

# class VaccinationCenter(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     working_hours = models.CharField(max_length=255)

# class VaccinationSlot(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)
#     slot_date = models.DateField()