from django import forms

from apps.internal.models import HospitalType


class HospitalTypeForm(forms.ModelForm):

    class Meta:
        model = HospitalType
        exclude = ()