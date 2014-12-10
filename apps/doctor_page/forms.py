# -*-coding:utf8-*-
from django import forms
from apps.internal.models import Doctor, DoctorUser, Hospital, Comment


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
#        fields = ['last_name', 'first_name', 'patronymic', 'sex', 'speciality', 'hospitals', 'image']


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = DoctorUser
#        fields = ['doctor']


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
#        fields = ['name', 'is_state', 'type', 'city', 'address', 'email', phone', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'content': forms.Textarea(),
        }
#        fields = ['content']
