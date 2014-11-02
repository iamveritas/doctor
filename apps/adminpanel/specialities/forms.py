from django import forms

from apps.internal.models import Speciality


class SpecialityForm(forms.ModelForm):

    class Meta:
        model = Speciality