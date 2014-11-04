from django import forms

from apps.internal.models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ()