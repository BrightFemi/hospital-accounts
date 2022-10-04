from django.urls import path
from .import  views

urlpatterns=[
     path('register/',views.register, name='register'),
     path('doctor-register/',views.doctor_register.as_view(), name='doctor-register'),
     path('patient-register/',views.patient_register.as_view(), name='patient-register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
]