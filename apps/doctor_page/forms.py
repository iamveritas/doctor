# -*-coding:utf8-*-
from django import forms
from apps.internal.models import Doctor, DoctorUser


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
#        fields = ['last_name', 'first_name', 'patronymic', 'sex', 'speciality', 'hospitals', 'image']


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = DoctorUser
#        fields = ['doctor']


