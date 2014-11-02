from django import forms

from apps.internal.models import Hospital


class HospitalForm(forms.ModelForm):

    class Meta:
        model = Hospital