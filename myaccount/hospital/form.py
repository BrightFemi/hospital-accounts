from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import Patient,Doctor,User

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length= 100, required=False)
    last_name = forms.CharField(max_length= 100, required=False)
    phone_number = forms.CharField(max_length= 100, required=False)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        patient = Patient.objects.create(user=user)
        patient.save()
        return user


class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length= 100, required=False)
    last_name = forms.CharField(max_length= 100, required=False)
    phone_number = forms.CharField(max_length= 100, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_doctor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.save()
        return user
