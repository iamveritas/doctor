from django import forms

from apps.internal.models import City


class CityForm(forms.ModelForm):

    class Meta:
        model = City
