"""
URL configuration for covid_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
from covid import statecity
from covid import category
from covid import doctor
from covid import patient
from covid import booking


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/statelist', statecity.State_List),
    re_path(r'^api/citylist', statecity.City_List),
    re_path(r'^api/centerlist', category.center_List),
    re_path(r'^api/categorylist', category.Category_List),
    re_path(r'^api/usersubmit', doctor.Submit_User),
    re_path(r'^api/patientsubmit',patient.Submit_User),
    re_path(r'^api/usersearch', patient.User_Search),
    re_path(r'^api/booking', booking.Submit_booking),
    re_path(r'^api/addcenter', category.add_center),
    re_path(r'^api/doctorlogin',doctor.Doctor_Login),

]
